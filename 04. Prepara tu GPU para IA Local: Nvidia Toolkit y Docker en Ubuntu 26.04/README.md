# Prepara tu GPU para IA Local: Nvidia Toolkit y Docker en Ubuntu 26.04

Si quieres correr modelos de Inteligencia Artificial localmente (como Ollama) o necesitas aceleración por hardware en tus contenedores de Docker, este tutorial es fundamental. Veremos la configuración exacta para que tu GPU, ya sea de escritorio o de laptop (como la serie RTX 4000), trabaje sin problemas y al máximo rendimiento con tus contenedores.


Despues de reiniciar ejecute el siguiente comando como un usuario sin privilegios para comprobar que todo funcione correctamente:

```bash
docker run --rm --gpus 1 --device /dev/nvidia0 --device /dev/nvidiactl --device /dev/nvidia-modeset --device /dev/nvidia-uvm --device /dev/nvidia-uvm-tools nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```


📌 Comandos utilizados en el video: [Link a tu blog, GitHub o Pinned Comment]

No olvides suscribirte y dejar un like si te sirvió el tutorial. ¡Cualquier duda, déjala en los comentarios!
