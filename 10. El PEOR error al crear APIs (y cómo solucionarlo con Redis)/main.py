from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import redis
import hashlib
import json
import uuid
import time
import os

app = FastAPI()

# Conexión a Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

class IdempotencyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Aplicar solo a mutaciones
        if request.method not in ["POST", "PATCH"]:
            return await call_next(request)
            
        idempotency_key = request.headers.get("Idempotency-Key")
        # Si no hay key, sigue el flujo normal sin protección
        if not idempotency_key:
            return await call_next(request)
            
        # Extraer body para generar el hash de seguridad
        body = await request.body()
        body_hash = hashlib.sha256(body).hexdigest()
        
        # Restaurar el body en el request para que el endpoint pueda leerlo
        async def receive(): return {"type": "http.request", "body": body}
        request._receive = receive
            
        # 2. Buscar si la operación ya existe o está en proceso
        cached_data_str = r.get(idempotency_key)
        if cached_data_str:
            cached_data = json.loads(cached_data_str)
            
            # Prevenir race conditions devolviendo 409 si está en proceso
            if cached_data.get("status") == "processing":
                return Response(
                    status_code=409, 
                    content=json.dumps({"error": "Request already processing. Retry later."}), 
                    headers={"Retry-After": "1"}
                )
                
            # Defensa contra robo/reuso de keys con datos diferentes
            if cached_data.get("body_hash") != body_hash:
                return Response(
                    status_code=422, 
                    content=json.dumps({"error": "Idempotency key reused with different body"})
                )
                
            # Devolver la respuesta guardada previamente
            return Response(
                content=cached_data["response_body"],
                status_code=cached_data["status_code"],
                media_type="application/json"
            )
            
        # 3. Bloqueo atómico (SET NX EX) con un TTL de 24 horas (86400s)
        processing_data = json.dumps({"status": "processing", "body_hash": body_hash})
        lock_acquired = r.set(idempotency_key, processing_data, nx=True, ex=86400)
        
        if not lock_acquired:
            return Response(
                status_code=409, 
                content=json.dumps({"error": "Concurrent request processing"}), 
                headers={"Retry-After": "1"}
            )

        # 4. Procesar la petición real
        response = await call_next(request)
        
        # Extraer la respuesta generada por nuestro endpoint
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk
            
        # Reconstruir la respuesta para FastAPI
        new_response = Response(content=response_body, status_code=response.status_code, 
                                headers=dict(response.headers), media_type=response.media_type)

        # 5. Reglas de Caché: Nunca cachear 5xx ni 408 (Timeouts)
        if response.status_code < 500 and response.status_code != 408:
            final_data = json.dumps({
                "status": "completed",
                "body_hash": body_hash,
                "response_body": response_body.decode('utf-8'),
                "status_code": response.status_code
            })
            r.set(idempotency_key, final_data, ex=86400) # Actualiza Redis con resultado final
        else:
            r.delete(idempotency_key) # Permite reintentar si el servidor falló
            
        return new_response

app.add_middleware(IdempotencyMiddleware)

@app.post("/pagar")
async def procesar_pago(request: Request):
    data = await request.json()
    amount = data.get("amount")
    
    # Simulamos una operación lenta (ej. conectar con pasarela de pago)
    time.sleep(3) 
    
    # El transaction_id será el mismo si es un reintento idempotente exitoso
    return {"mensaje": f"Cobro exitoso de {amount} USD", "transaction_id": str(uuid.uuid4())}
