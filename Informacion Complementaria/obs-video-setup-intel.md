# Configuración de OBS para Grabación y Transmisión

Esta es la configuración óptima que utilizo para grabar y transmitir en vivo desde OBS en Ubuntu.

## Salida
### Pestaña emisión
* Pista de audio: 1
* Codificador de audio: FFmpeg AAC
* Pista VOD: 2
* Codificador de video: FFmpeg VAAPI H.264
* Cambiar escala de salida: deshabilitado

### Ajustes de codificación (Emisión):
* Perfil: high
* Nivel: auto
* Control de frecuencia: QP Constante (CQP)
* QP Constannte: 20
* Intervalo de fotogramas claves: 0s

> **Multi-Streaming:** Transmito el perfil principal a Twitch y utilizo el plugin OBS Multi-RTMP para enviar una señal simultánea a YouTube.

-----------------------------------------------------

### Pestaña grabación
* Formato de grabación: MP4 fragmentado (.mp4)
* Codificador de video: FFmpeg VAAPI H.264
* Codificador de audio: FFmpeg AAC
* Pista de audio: 1
* Cambiar escala de salida: deshabilitado

### Ajustes de codificación (Grabación):
* Perfil: high
* Nivel: auto
* Control de frecuencia: QP Constante (CQP)
* QP Constannte: 23
* Intervalo de fotogramas claves: 2s

-----------------------------------------------------

## Audio
* Frecuencia de muestreo: 44.1 khz
* Canales: estéreo

-----------------------------------------------------

## Video
* Resolución de la base (lienzo): 3840x2160
* Resolución de salida (escalada): 3840x2160
* Valor fraccional de FPS: 60

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
