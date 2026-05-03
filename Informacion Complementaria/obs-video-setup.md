Esta es la configuracion que utilizo para grabrar y transmitir en vivo desde OBS

## Salida
### Pestana emision
* Pista de audio: 1
* codificador de audio: FFmpeg AAC
* Pista VOD: 2
* Codificador de video: nvidia nvenc h.264
* cambiar escala de salida: deshabilitado

### Ajustes de codificacion:
* control de frecuencia: tasa de bits constante
* tasa de bits: 7500 kbps
* intervalo de fotogramas claves: 2s
* preajuste: p5
* ajuste: calidad alta
* modo multipaso: pase unico
* perfil: high
* mirar hacia adelante: OFF
* cuantizacion adaptativa: ON
* B-Frames: 2

-----------------------------------------------------

### Pestana grabacion
* formato de grabacion: video matroska (mkv)
* codificador de video: nvidia nvenc av1
* codificador de audio: FFmpeg AAC
* pista de audio: 1
* cambiar escala de salida: deshabilitado

### Ajustes de codificacion:
* control de frecuencia: tasa de bits constante
* tasa de bits: 10000 kbps
* intervalo de fotogramas claves: 2s
* preajuste: p5
* ajuste: calidad alta
* modo multipaso: dos pasos
* perfil: main
* mirar hacia adelante: ON
* cuantizacion adaptativa: ON
* B-Frames: 2
* referencia de b-frames: deshabilitado

-----------------------------------------------------

## Audio
* frecuencia de muestreo: 44.1 khz
* canales: estereo

-----------------------------------------------------

## Video
* resolucion de la base (lienzo): 1920x1080
* resolucion de salida (escalada): 1920x1080
* valor fraccional de FPS: 60
* denominador: 1

## Avanzado
### red:
* cambiar dinamicamente la tasa de bits para gestionar la congestion: ON

