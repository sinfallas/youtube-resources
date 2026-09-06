import asyncio
import httpx
import uuid

async def disparar_peticiones_concurrentes():
    url = "http://api:8000/pagar"

    # 1. Generamos UNA sola llave de idempotencia para simular la MISMA transacción repetida
    llave_idempotencia = str(uuid.uuid4())
    headers = {"Idempotency-Key": llave_idempotencia}
    payload = {"amount": 100}

    print(f"Iniciando prueba de estrés con Idempotency-Key: {llave_idempotencia}")
    print("=" * 60)

    # httpx.AsyncClient maneja las conexiones asíncronas de manera eficiente
    async with httpx.AsyncClient(timeout=10.0) as client:
        # 2. Preparamos 5 peticiones idénticas simulando un error en el frontend
        # (ej. un usuario haciendo doble o triple clic muy rápido en el botón de pago)
        tareas = [
            client.post(url, headers=headers, json=payload)
            for _ in range(5)
        ]

        # 3. Disparamos todas las peticiones exactamente al mismo tiempo usando asyncio.gather
        print("Disparando 5 peticiones concurrentes al mismo milisegundo...\n")
        respuestas = await asyncio.gather(*tareas, return_exceptions=True)

        # 4. Mostramos los resultados de cada petición
        for i, r in enumerate(respuestas):
            if isinstance(r, Exception):
                print(f"Petición {i+1} | Falló con Error: {str(r)}")
            else:
                print(f"Petición {i+1} | Status: {r.status_code} | Respuesta: {r.text}")

if __name__ == "__main__":
    # Ejecutamos el event loop principal
    asyncio.run(disparar_peticiones_concurrentes())
