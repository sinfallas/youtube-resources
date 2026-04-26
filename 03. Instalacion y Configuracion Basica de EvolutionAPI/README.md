# Instalacion y Configuracion Basica de EvolutionAPI

URL del Instalador con Docker: https://github.com/tecno-consultores/llm-lab/

## Pasos a seguir:

* Al entrar a la url presione el boton verde que dice Code y selecciones HTTPS, luego copie la informacion que le muestra debajo.
* Vaya a su instancia de GNU/Linux en donde quiere realizar la instalacion y coloque el siguiente comando:

```bash
git clone https://github.com/tecno-consultores/llm-lab.git
```

* Luego entre al repositorio recien clonado mediante el comando cd

```bash
cd llm-lab
```

* Alli edite el archivo env.example para cambiar la url de evolutionapi:

```bash
nano env.example
```

* Ubique la linea: EVOLUTION_SERVER_URL=https://evo.example.com #change me
* Reemplace la url de ejemplo con la que va a utilizar
* Ubique la linea: evoapikey=GSAQM73l6zcFYAECYfPUIaB9iCfjTCOp #change me
* Reemplace por una cadena de caracteres al azar, solo letras y numeros
* Guarde con Ctrl + o y luego Ctrl + x para salir
* Luego ejecute el siguiente comando para descargar las imagenes de docker neecsarias:

```bash
docker compose -f docker-compose.yml --env-file env.example --profile evolutionapi pull
```

* Al finalizar la descarga puede iniciar el servicio mediante el siguiente comando:

```bash
docker compose -f docker-compose.yml --env-file env.example --profile evolutionapi up -d
```

* Vaya a su navegador y acceda a la url del manager para proceder con la configuracion: https://evo.example.com/manager
* Una vez dentro de la GUI cree una nueva instancia, recuerde que el Channel debe ser **Baileys**
* Haga clic en el icono del **engrane** para acceder a la configuracion.
* Haga clic en en el menu de **Configurations** a la izquierda de la pantalla, luego en **settings** y marque las siguientes casillas:
- reject calls
- ignore groups
- always online
- read messages

* Presione **save** para guardar
* Ahora vaya a **Events**, luego a **webhook**, alli coloque la url del webhook y marque las siguientes casillas:
- enable
- webhook base64
- message upsert
* Presione **save** para guardar
* Para finalizar vaya a **Dashboard** y haga clic en el boton **restart** y luego en el boton amarillo llamado **Get QR Code**
