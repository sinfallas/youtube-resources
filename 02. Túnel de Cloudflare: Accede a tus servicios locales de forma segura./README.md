# Túnel de Cloudflare: Acceso Seguro a Servicios Locales

Este repositorio contiene el material complementario del video tutorial "Túnel de Cloudflare: Accede a tus servicios locales de forma segura". Aquí encontrarás los comandos y archivos de configuración necesarios para exponer tus servicios locales a internet de forma segura, sin abrir puertos en tu router y protegiendo tu IP pública mediante la infraestructura de Cloudflare Zero Trust.


## Instalación Rápida (CLI)

Si prefieres instalar el conector directamente en tu sistema operativo, una vez creado el túnel en el panel de Cloudflare, utiliza el siguiente comando (reemplaza TUNNEL_TOKEN con el tuyo):


## Ejemplo para Linux / Debian / Ubuntu

Los siguientes comandos deben ejecutarse como root:

* Creamos la carpeta para la firma.

```bash
mkdir -p --mode=0755 /usr/share/keyrings
```

* Descargamos la llave desde el servidor.

```bash
curl -fsSL https://pkg.cloudflare.com/cloudflare-public-v2.gpg | tee /usr/share/keyrings/cloudflare-public-v2.gpg >/dev/null
```
* Creamo el archivo para el repositorio desde donde se hara la instalacion.

```bash
echo 'deb [signed-by=/usr/share/keyrings/cloudflare-public-v2.gpg] https://pkg.cloudflare.com/cloudflared any main' | tee /etc/apt/sources.list.d/cloudflared.list
```
* Instalamos el paquete.

```bash
apt-get update && apt-get install cloudflared
```
* Iniciamos el servicio.

```bash
cloudflared service install TUNNEL_TOKEN
```

---

🐳 Alternativa con Docker (Recomendado)

Si prefieres mantener tu entorno limpio, puedes ejecutar el conector de Cloudflare como un contenedor persistente.

En esta carpeta encontrarás un archivo docker-compose.yml. Para levantarlo, solo necesitas configurar tu token en las variables de entorno:
Instrucciones:

* Edita el archivo docker-compose.yml.

* Sustituye TUNNEL_TOKEN por el token proporcionado por Cloudflare.

* Ejecuta el comando:

```bash
docker-compose up -d
```
---

📂 Contenido del Repo

* /docker-compose.yml: Configuración lista para desplegar el túnel como servicio.

* comandos.txt: Notas rápidas sobre la gestión del servicio cloudflared.
