# Laboratorio de Idempotencia en API

Este repositorio contiene una demostración práctica de un middleware de idempotencia construido con FastAPI y Redis. Está diseñado para proteger operaciones críticas (como pagos) contra problemas de red, dobles clics y fallos temporales del servidor.

## Principales componentes
Se incorpora una funcion para que el laboratorio se comporte de manera realista bajo estrés:
- **Cliente Redis Asíncrono (`redis.asyncio`)**: En lugar de bloquear el *Event Loop* en cada operación de lectura/escritura de llaves, el middleware ahora funciona 100% de manera no bloqueante.
- **Simulación concurrente (`asyncio.sleep`)**: El simulador de latencia bancaria ya no bloquea todo el proceso del servidor. Esto es clave si intentas hacer pruebas de estrés (benchmark) locales simulando alto tráfico.
- **Cliente de Pruebas Integrado (`httpx`)**: Se incluye un contenedor dedicado que utiliza `httpx` de forma asíncrona para disparar peticiones simultáneas reales hacia el servidor y probar las condiciones de carrera (Race Conditions).
- **Documentación de Laboratorio**: Se añadieron comentarios detallados en `main.py` explicando el propósito pedagógico de la latencia y los fallos aleatorios.

## Requisitos Previos
- Docker y Docker Compose instalados.
- Levantar la infraestructura en segundo plano (API, Redis y el contenedor Tester):
  ```bash
  docker compose up -d --build
  ```
> **Nota de Infraestructura**: Para un entorno de producción o staging, es fundamental modificar el archivo `docker-compose.yml` para añadir persistencia a Redis (mediante un *Volume* y el flag `--appendonly yes`), así no se pierden las llaves de idempotencia al reiniciar los contenedores.

---

## Escenarios de Prueba

### Pruebas Básicas (Usando cURL)

#### 1. Petición Inicial (Primer Intento)
Envía un pago con una llave de idempotencia nueva. Notarás un retraso de ~2 segundos simulando la conexión al banco. Debido a la simulación de fallos (50% de probabilidad), puede que te devuelva un `200 OK` o un `500 Internal Server Error`.

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: ebc8d507-68b5-4b8c-a7c8-04b39b03ebdf" \
  -d '{"amount": 100}'
```

#### 2. Reintento Idéntico (Recarga manual o fallo de red)
Si la petición anterior fue exitosa (`200 OK`), vuelve a ejecutar exactamente el mismo comando.
La respuesta será **instantánea** y devolverá exactamente el mismo `transaction_id`, demostrando que el código del endpoint no se volvió a ejecutar (evitando un doble cobro).

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: ebc8d507-68b5-4b8c-a7c8-04b39b03ebdf" \
  -d '{"amount": 100}'
```

#### 3. Cambio de Datos bajo la misma Llave (Protección Hash)
Intenta reusar la misma llave anterior pero cambiando el monto a `500`. El sistema detectará que el cuerpo de la petición cambió (validación criptográfica del payload) y devolverá un `422 Unprocessable Entity` para evitar el robo o reuso indebido de llaves.

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: ebc8d507-68b5-4b8c-a7c8-04b39b03ebdf" \
  -d '{"amount": 500}'
```

#### 4. Simulación de Fallo de Servidor y Reintento (Manejo de 5xx)
Envía una petición con una nueva llave. Como el código tiene un 50% de probabilidad de fallar simulando una caída del servidor, repite el comando hasta obtener un `500 Internal Server Error`.
Luego, vuelve a intentarlo con la misma llave. Verás que el servidor te permite reintentar la operación (limpió la llave fallida de Redis) hasta que finalmente pase y obtengas el `200 OK`.

```bash
curl -i -X POST http://localhost:8000/pagar \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: fallo-test-001" \
  -d '{"amount": 100}'
```

---

### Prueba Avanzada de Estrés

#### 5. Simular un Doble Clic Concurrente (Protección de Race Conditions)
Para comprobar que el candado de Redis es capaz de evitar operaciones simultáneas idénticas (como cuando un usuario da varios clics al botón de pago por desesperación o un bug en el frontend repite llamadas en paralelo), utilizaremos nuestro contenedor `tester`.

Este contenedor ejecuta el script `test_cliente.py`, el cual dispara **5 peticiones asíncronas en el mismo milisegundo**.

**Comando (Puedes ejecutarlo cuantas veces quieras):**
```bash
docker exec -it tester python test_cliente.py
```

**Resultado esperado:** 
Verás en la terminal que una de las peticiones es aceptada para su procesamiento (quedando en espera los 2 segundos de la simulación del banco), mientras que las otras 4 peticiones rebotan de forma inmediata con un estado HTTP `409 Conflict`, previniendo así cualquier cobro duplicado.

---

## Herramientas de Depuración (Inspección de Redis)

Se han agregado endpoints específicos para monitorear el comportamiento del almacenamiento en caché durante las pruebas. Esto te permite verificar qué transacciones están en proceso, cuáles se han completado y limpiar el entorno rápidamente.

### 1. Listar todas las llaves activas
Muestra todas las llaves de idempotencia almacenadas en Redis, junto con su estado (`processing` o `completed`) y el tiempo de vida restante (TTL).

**Comando:**
```bash
curl -X 'GET' 'http://localhost:8000/debug/idempotency'
```

### 2. Inspeccionar una llave específica
Busca una llave exacta para auditar su contenido, incluyendo el hash de seguridad y la respuesta original guardada (si ya finalizó). Reemplaza `<TU_LLAVE>` con el valor de tu `Idempotency-Key`.

**Comando:**
```bash
curl -X 'GET' 'http://localhost:8000/debug/idempotency/<TU_LLAVE>'
```

### 3. Limpiar toda la caché (Botón de pánico)
Elimina todas las llaves almacenadas en la base de datos de Redis. Útil para reiniciar el laboratorio tras simulaciones masivas de errores.

**Comando:**
```bash
curl -X 'DELETE' 'http://localhost:8000/debug/idempotency'
```
