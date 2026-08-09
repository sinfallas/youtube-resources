# Convierte tu MikroTik en un escudo contra virus y publicidad

URL del video en Youtube: 

¿Cansado de la publicidad invasiva y los sitios peligrosos en tu red? En este tutorial, te enseño a configurar listas de bloqueo (adlists) en tu router MikroTik utilizando los recursos de Firebog. Aprenderás a automatizar el filtrado de DNS de forma profesional, mejorando la seguridad y la velocidad de carga en todos tus dispositivos sin instalar software adicional.

**Requisito de versión:** Disponible a partir de la versión **RouterOS 7.15**.

Este documento proporciona los pasos para preparar tu router MikroTik para usar DNS over HTTPS (DoH) y la función de Adlist para bloqueo de dominios.

## 1. Descargar e Instalar Certificados Raíz
Para que tu router valide de forma segura la conexión al servidor DoH, es necesario descargar e instalar los certificados CA más recientes.

```routeros
/tool fetch url="[https://curl.se/ca/cacert.pem](https://curl.se/ca/cacert.pem)" check-certificate=no
/certificate import file-name=cacert.pem passphrase=""
```

## 2. Ajustar el Tamaño de Caché DNS
La función Adlist almacena las listas en la caché DNS del router. Para evitar problemas de falta de memoria al cargar listas grandes, asignamos 64 MB (65536 KiB) de caché.

```routeros
/ip dns set cache-size=65536
```

## 3. Crear Registros DNS Estáticos
Antes de establecer el túnel DoH con Cloudflare, el router necesita resolver el dominio `cloudflare-dns.com`. Estas reglas estáticas le indican al router las IP exactas a consultar.

```routeros
/ip dns static add name=cloudflare-dns.com address=1.1.1.1
/ip dns static add name=cloudflare-dns.com address=1.0.0.1
/ip dns static add name=cloudflare-dns.com address=2606:4700:4700::1111
/ip dns static add name=cloudflare-dns.com address=2606:4700:4700::1001
```

## 4. Listas de Bloqueo (Adlist)
Puedes obtener las URLs con las mejores listas para bloquear publicidad, rastreadores y malware en la siguiente página:

* **URL para bajar las listas:** [https://firebog.net/](https://firebog.net/)

Y agregarla de la siguiente forma:

```routeros
/ip dns adlist add url="https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts" ssl-verify=yes
```
---

*Nota: Para habilitar el DoH una vez completados estos pasos, puedes usar:*

```routeros
/ip dns set use-doh-server=https://cloudflare-dns.com/dns-query verify-doh-cert=yes
```
