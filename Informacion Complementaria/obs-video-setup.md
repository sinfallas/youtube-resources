Esta es la configuración que utilizo para grabar y transmitir en vivo desde OBS

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
* mirar hacia adelante: OFF
* cuantización adaptativa: ON
* B-Frames: 2

-----------------------------------------------------

### Pestaña grabación
* formato de grabación: video matroska (mkv)
* codificador de video: nvidia nvenc av1
* codificador de audio: FFmpeg AAC
* pista de audio: 1
* cambiar escala de salida: deshabilitado

### Ajustes de codificación:
* control de frecuencia: tasa de bits constante
* tasa de bits: 10000 kbps
* intervalo de fotogramas claves: 2s
* preajuste: p5
* ajuste: calidad alta
* modo multipaso: dos pasos
* perfil: main
* mirar hacia adelante: ON
* cuantización adaptativa: ON
* B-Frames: 2
* referencia de b-frames: deshabilitado

-----------------------------------------------------

## Audio
* frecuencia de muestreo: 44.1 khz
* canales: estéreo

-----------------------------------------------------

## Video
* resolución de la base (lienzo): 1920x1080
* resolución de salida (escalada): 1920x1080
* valor fraccional de FPS: 60
* denominador: 1
* Filtro de reducción: Lanczos (escalado fino, 36 muestras).

## Avanzado

### video:
* formato de color: NV12
* espacio de color: Rec. 709
* gama de colores: Limitado
* nivel de blanco sdr: 300
* nivel de pico nominal HDR: 1000

### red:
* cambiar dinámicamente la tasa de bits para gestionar la congestión: ON

