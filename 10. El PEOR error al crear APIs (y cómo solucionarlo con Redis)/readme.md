# Laboratorio de Idempotencia en API

Este repositorio contiene una demostración práctica de un middleware de idempotencia construido con FastAPI y Redis. Está diseñado para proteger operaciones críticas (como pagos) contra problemas de red, dobles clics y fallos temporales del servidor.

## Requisitos Previos
- Docker y Docker Compose instalados.
- Levantar la infraestructura en segundo plano:
  ```bash
  docker compose up -d --build
  ```

---

## Escenarios de Prueba (Usando cURL)

### 1. Petición Inicial (Primer Intento)
Envía un pago con una llave de idempotencia nueva. Notarás un retraso de ~2 segundos simulando la conexión al banco. Debido a la simulación de fallos, puede que te devuelva un `200 OK` o un `500 Internal Server Error`.

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: ebc8d507-68b5-4b8c-a7c8-04b39b03ebdf" \
  -d '{"amount": 100}'
```

### 2. Reintento Idéntico (Recarga manual o fallo de red)
Si la petición anterior fue exitosa (`200 OK`), vuelve a ejecutar exactamente el mismo comando.
La respuesta será **instantánea** y devolverá exactamente el mismo `transaction_id`, demostrando que el código del endpoint no se volvió a ejecutar (evitando un doble cobro).

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: ebc8d507-68b5-4b8c-a7c8-04b39b03ebdf" \
  -d '{"amount": 100}'
```

### 3. Cambio de Datos bajo la misma Llave (Protección Hash)
Intenta reusar la misma llave anterior pero cambiando el monto a `500`. El sistema detectará que el cuerpo de la petición cambió y devolverá un `422 Unprocessable Entity` para evitar el robo o reuso indebido de llaves.

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: ebc8d507-68b5-4b8c-a7c8-04b39b03ebdf" \
  -d '{"amount": 500}'
```

### 4. Simulación de Fallo de Servidor y Reintento (Manejo de 5xx)
Envía una petición con una nueva llave. Como el código tiene un 50% de probabilidad de fallar simulando una caída del servidor, repite el comando hasta obtener un `500 Internal Server Error`.
Luego, vuelve a intentarlo con la misma llave. Verás que el servidor te permite reintentar la operación (limpió la llave fallida de Redis) hasta que finalmente pase y obtengas el `200 OK`.

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: fallo-test-001" \
  -d '{"amount": 100}'
```

### 5. Simular un Doble Clic Concurrente (Protección de Race Conditions)
Genera un nuevo intento lanzando dos peticiones exactamente al mismo tiempo (usando `&` para mandar la primera a segundo plano). 
Una petición se procesará normalmente (esperando los 2 segundos) y la otra será rechazada de inmediato con un `409 Conflict`, evitando el doble cobro simultáneo.

```bash
curl -i -X POST http://localhost:8000/pagar -H "Idempotency-Key: doble-clic-123" -H "Content-Type: application/json" -d '{"amount": 50}' & \
curl -i -X POST http://localhost:8000/pagar -H "Idempotency-Key: doble-clic-123" -H "Content-Type: application/json" -d '{"amount": 50}'
```
