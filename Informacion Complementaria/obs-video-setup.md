Esta es la configuración que utilizo para grabar y transmitir en vivo desde OBS con una GPU NVIDIA, varias de las configuraciones aparecen apagadas porque utilizan CUDA y si van a grabar videos y usar IA al mismo tiempo (por ejemplo: ollama) lo mejor es dedicar los cuda cores para IA.

## Salida
### Pestaña emisión
* Pista de audio: 1
* codificador de audio: FFmpeg AAC
* Pista VOD: 2
* Codificador de video: nvidia nvenc h.264
* cambiar escala de salida: deshabilitado

### Ajustes de codificación:
* control de frecuencia: tasa de bits constante
* tasa de bits: 7500 kbps
* intervalo de fotogramas claves: 2s
* preajuste: p5
* ajuste: calidad alta
* modo multipaso: pase único
* perfil: high
* mirar hacia adelante: OFF (Utiliza CUDA)
* cuantización adaptativa: OFF (Utiliza CUDA)
* B-Frames: 2

-----------------------------------------------------

### Pestaña grabación
* formato de grabación: MP4 fragmentado (.mp4)
* codificador de video: nvidia nvenc av1
* codificador de audio: FFmpeg AAC
* pista de audio: 1
* cambiar escala de salida: deshabilitado

### Ajustes de codificación:
* control de frecuencia: QP Constante
* QP constannte: 20
* intervalo de fotogramas claves: 2s
* preajuste: p4
* ajuste: calidad alta
* modo multipaso: Pase unico (dos pasos utiliza CUDA)
* perfil: main
* mirar hacia adelante: OFF (Utiliza CUDA)
* cuantización adaptativa: OFF (Utiliza CUDA)
* B-Frames: 2
* referencia de b-frames: deshabilitado

-----------------------------------------------------

## Audio
* frecuencia de muestreo: 44.1 khz
* canales: estéreo

-----------------------------------------------------

## Video
* resolución de la base (lienzo): 3840x2160
* resolución de salida (escalada): 3840x2160
* valor fraccional de FPS: 60
* denominador: 1

-----------------------------------------------------

## Avanzado

### video:
* formato de color: NV12
* espacio de color: Rec. 709
* gama de colores: Limitado
* nivel de blanco sdr: 300
* nivel de pico nominal HDR: 1000

### grabacion:
* convertir automaticamente a mp4: OFF

### red:
* cambiar dinámicamente la tasa de bits para gestionar la congestión: ON

