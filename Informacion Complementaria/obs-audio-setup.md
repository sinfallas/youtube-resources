Para lograr una calidad de voz profesional, limpia y perfecta para grabar tutoriales o explicaciones técnicas, el secreto está en configurar una cadena de filtros dentro de OBS.

El orden de los filtros es crucial, ya que el audio pasa por ellos de arriba hacia abajo. Aquí tienes la configuración ideal, paso a paso, utilizando los filtros nativos de OBS:

1. Eliminación de ruido (Noise Suppression)
    * Propósito: Eliminar el zumbido de fondo constante.
    * Método: Al agregar el filtro, selecciona el método RNNoise (buena calidad, mayor uso de CPU). Este filtro utiliza inteligencia artificial para distinguir tu voz del ruido de fondo y es sumamente efectivo. Si notas que consume demasiados recursos del sistema, cambia a Speex y ajusta el nivel manualmente hasta que el ruido de fondo desaparezca sin afectar tu voz.
2. Puerta de ruido (Noise Gate)
    * Propósito: Silenciar el micrófono por completo cuando no estás hablando, evitando que se cuelen ruidos molestos entre tus frases.
    * Ajustes base:
        + Umbral de clausura (Close Threshold): -40 dB (cuando el volumen baje de este punto, el micro se silencia).
        + Umbral de apertura (Open Threshold): -30 dB (debes hablar más fuerte que este nivel para que el micro se abra).
        + Tip de ajuste: Quédate en absoluto silencio y observa la barra del mezclador de audio en OBS. Identifica hasta dónde llega el ruido de fondo y configura el "Umbral de clausura" un par de decibelios por encima de ese ruido.
3. Ecualizador de 3 bandas (3-Band Equalizer)
    * Propósito: Darle más "cuerpo" y claridad a tu voz. El GM301 puede sonar un poco plano de fábrica.
    * Ajustes base:
        + Altos (Highs): +2.0 dB a +3.0 dB (aporta claridad para que las palabras se entiendan mejor).
        + Medios (Mids): -1.0 dB a 0 dB (reducir ligeramente los medios evita que la voz suene como si estuvieras dentro de una caja).
        + Bajos (Lows): +1.5 dB a +2.5 dB (añade calidez y presencia, similar al tono de los locutores de radio).
4. Compresor (Compressor)
    * Propósito: Nivelar el volumen general. Hace que tus partes más suaves suenen un poco más fuertes y atenúa los picos si de repente hablas muy alto. Mantiene tu voz en un nivel constante para el espectador.
    * Ajustes base:
        + Relación (Ratio): 3:1 o 4:1
        + Umbral (Threshold): -18 dB (ajusta esto para que el compresor empiece a actuar solo cuando hables a tu volumen normal).
        + Ataque (Attack): 2 ms
        + Liberar (Release): 100 ms
        + Ganancia de salida (Output Gain): +2 dB a +4 dB (para recuperar el volumen general que reduce la compresión).
5. Limitador (Limiter)
    * Propósito: Es tu red de seguridad final. Evita que el audio sature o "clipee" (cuando la barra llega al rojo y distorsiona) si se produce un ruido fuerte inesperado.
    * Ajustes base:
        + Umbral (Threshold): -3.0 dB (el volumen de tu transmisión o grabación jamás pasará de este punto).
        + Liberación (Release): 60 ms

## Un apunte sobre el entorno físico:

Los filtros de software hacen magia, pero la física manda. Asegúrate de tener el microfono a una distancia de 15 a 20 centímetros de tu boca. Si lo colocas más lejos (por ejemplo, al lado del monitor), te verás obligado a subir la ganancia, lo que introducirá mucho más ruido de habitación que los filtros tendrán dificultades para eliminar sin distorsionar tu voz. Apunta siempre a que, al hablar normalmente, tu nivel de audio en el mezclador de OBS fluctúe en la zona amarilla (entre -15 dB y -9 dB).

### Problemas de cortes en el audio:

Cuando el audio se corta al inicio de las frases, es un comportamiento típico de una configuración muy agresiva en la Puerta de ruidos (Noise Gate). Este filtro está diseñado para silenciar el micrófono cuando no hablas, pero si los umbrales no están bien ajustados, el micrófono tarda en "despertar" y se "come" la primera sílaba.

Aquí tienes los pasos para solucionarlo:

1. Ajusta el Umbral de apertura (Open Threshold): El valor de -30 dB sugerido originalmente puede ser demasiado alto para tu tono de voz natural al empezar a hablar.
    + Acción: Baja el Umbral de apertura a un valor menor, por ejemplo, -35 dB o -38 dB.
    + Objetivo: Al bajar este número, permites que sonidos más suaves (como el inicio de una palabra) activen el micrófono con mayor facilidad.
2. Revisa el tiempo de "Ataque" (Attack): Aunque no se detalló específicamente en los ajustes base del archivo, la Puerta de Ruidos en OBS tiene un parámetro llamado Ataque.
    + Acción: Asegúrate de que el tiempo de Ataque sea muy bajo (entre 1 ms y 5 ms).
    + Objetivo: Esto determina qué tan rápido se abre el micrófono una vez que detecta tu voz. Si es muy alto, el corte inicial será muy notorio.
3. Verifica la distancia física y la ganancia: Si el micrófono está demasiado lejos, la señal que llega es débil y no alcanza a superar el umbral de apertura con rapidez.
    + Distancia: Confirma que el Redragon GM301 esté a una distancia de entre 15 y 20 centímetros de tu boca.
    + Ganancia: Si el audio sigue cortándose, aumenta ligeramente la Ganancia de salida en el filtro de Compresor (por ejemplo, a +4 dB o +5 dB) para que la señal general sea más robusta antes de llegar a los límites finales.
4. Prueba de validación: Quédate en silencio y observa la barra del mezclador en OBS. Habla de forma pausada y suave.
    + Si la barra tarda en reaccionar, sigue bajando el Umbral de apertura.
    + Apunta a que tu voz fluctúe siempre en la zona amarilla (entre -15 dB y -9 dB) para asegurar una captura constante.

