# Configuración de OBS para Grabación y Transmisión

Esta es la configuración óptima que utilizo para grabar y transmitir en vivo desde OBS en mi laptop Asus TUF A15 con Ubuntu, aprovechando el codificador de la RTX 4060. Esta configuración está pensada para obtener la **máxima calidad de video** en tutoriales estándar donde OBS no compite por los recursos de la tarjeta gráfica (CUDA).

> **💡 Nota para tutoriales sobre Inteligencia Artificial (ej. Ollama, Modelos Locales):**
> Si vas a ejecutar modelos de IA localmente mientras grabas, es indispensable liberar los núcleos CUDA de la GPU para que el rendimiento de la IA y del sistema no se vea afectado. Para ello, realiza estos ajustes en tu OBS:
> - **Emisión:** Cambia la *Cuantización adaptativa* a OFF.
> - **Grabación:** Cambia el *Modo multipaso* a Pase único (el modo de dos pasos utiliza CUDA).
> - **Grabación:** Cambia *Mirar hacia adelante* y *Cuantización adaptativa* a OFF.
> - **Grabación (Opcional pero recomendado):** Reduce el *Preajuste* de p5 a p4 y cambia el *Control de frecuencia* a QP Constante en 20 para aligerar la carga general de la GPU.

## Salida
### Pestaña emisión
* Pista de audio: 1
* Codificador de audio: FFmpeg AAC
* Pista VOD: 2
* Codificador de video: nvidia nvenc h.264
* Cambiar escala de salida: deshabilitado

### Ajustes de codificación (Emisión):
* Control de frecuencia: tasa de bits constante (CBR)
* Tasa de bits: 7500 kbps
* Intervalo de fotogramas claves: 2s
* Preajuste: p5
* Ajuste: calidad alta
* Modo multipaso: dos pasos (Mejora la distribución del bitrate usando CUDA) (resolución de un cuarto)
* Perfil: high
* Mirar hacia adelante: ON (Mejora el manejo de escenas dinámicas usando CUDA)
* Cuantización adaptativa: ON
* B-Frames: 2

> **Multi-Streaming:** Transmito el perfil principal a Twitch y utilizo el plugin OBS Multi-RTMP para enviar una señal simultánea a YouTube.

-----------------------------------------------------

### Pestaña grabación
* Formato de grabación: MP4 fragmentado (.mp4)
* Codificador de video: nvidia nvenc av1
* Codificador de audio: FFmpeg AAC
* Pista de audio: 1
* Cambiar escala de salida: deshabilitado

### Ajustes de codificación (Grabación):
* Control de frecuencia: tasa de bits constante (CBR)
* Tasa de bits: 10000 kbps
* Intervalo de fotogramas claves: 2s
* Preajuste: p5
* Ajuste: calidad alta
* Modo multipaso: dos pasos (Maximiza la calidad usando CUDA) (resolución de un cuarto)
* Perfil: main
* Mirar hacia adelante: ON (Mejora el manejo de B-frames usando CUDA)
* Cuantización adaptativa: ON
* B-Frames: 2
* Referencia de b-frames: deshabilitado

-----------------------------------------------------

## Audio
* Frecuencia de muestreo: 44.1 khz
* Canales: estéreo

-----------------------------------------------------

## Video
* Resolución de la base (lienzo): 3840x2160
* Resolución de salida (escalada): 3840x2160
* Valor fraccional de FPS: 60
* Denominador: 1
* Filtro de reducción: Bicúbico (Escalado fino, 16 muestras)

-----------------------------------------------------

## Avanzado

### Video:
* Formato de color: NV12
* Espacio de color: Rec. 709
* Gama de colores: Limitado
* Nivel de blanco SDR: 300
* Nivel de pico nominal HDR: 1000

### Grabación:
* Convertir automáticamente a mp4: OFF

### Red:
* Cambiar dinámicamente la tasa de bits para gestionar la congestión: ON
