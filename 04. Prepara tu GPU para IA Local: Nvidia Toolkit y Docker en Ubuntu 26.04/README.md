# Prepara tu GPU para IA Local: Nvidia Toolkit y Docker en Ubuntu 26.04

Si quieres correr modelos de Inteligencia Artificial localmente (como Ollama) o necesitas aceleración por hardware en tus contenedores de Docker, este tutorial es fundamental. Veremos la configuración exacta para que tu GPU, ya sea de escritorio o de laptop (como la serie RTX 4000), trabaje sin problemas y al máximo rendimiento con tus contenedores.


Despues de reiniciar ejecute el siguiente comando como un usuario sin privilegios para comprobar que todo funcione correctamente:

```bash
docker run --rm --gpus 1 --device /dev/nvidia0 --device /dev/nvidiactl --device /dev/nvidia-modeset --device /dev/nvidia-uvm --device /dev/nvidia-uvm-tools nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```


📌 Comandos utilizados en el video: 

* para clonar el repositorio de laboratorio

```bash
git clone https://github.com/tecno-consultores/llm-lab.git
```
* para ejecutar ollama

```bash
docker compose -f docker-compose.yml --env-file env.example --profile ollama-gpu up -d
```
* para entrar al contenedor de ollama

```bash
docker exec -it ollama bash
```
* para descargar gemma4:e2b

```bash
ollama pull gemma4:e2b
```

* para ejecutar gemma4:e2b

```bash
ollama run gemma4:e2b
```
* para salir del chat escribe: /bye y luego exit para regresar al terminal de tu ubuntu

* para desinstalar ollama ejecuta:

```bash
docker compose -f docker-compose.yml --env-file env.example --profile ollama-gpu down
```

No olvides suscribirte y dejar un like si te sirvió el tutorial. ¡Cualquier duda, déjala en los comentarios!
