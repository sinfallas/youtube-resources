# Tu proveedor de Internet te ESPÍA (Evítalo con MikroTik y DoH)

¿Sabías que tu proveedor de internet (ISP) puede ver y registrar cada página web que visitas, incluso en modo incógnito? En este video te enseño cómo blindar tu privacidad configurando DNS over HTTPS (DoH) usando Cloudflare en tu router MikroTik.

Aprenderás paso a paso cómo encriptar tus peticiones DNS para que nadie pueda rastrear tu actividad en la red. Esta configuración de seguridad de nivel empresarial es fácil de aplicar y vital para tu red local.

## 1. Configurar NTP para sincronizar la hora (requerido para validar certificados)
```routeros
/system ntp client set enabled=yes servers=0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org,3.pool.ntp.org
```

## 2. Descargar e importar certificados raiz
```routeros
/tool fetch url="https://curl.se/ca/cacert.pem" check-certificate=no
/certificate import file-name=cacert.pem passphrase=""
```

## 3. Crear registros estáticos para resolver Cloudflare
```routeros
/ip dns static add name=cloudflare-dns.com address=1.1.1.1
/ip dns static add name=cloudflare-dns.com address=1.0.0.1
/ip dns static add name=cloudflare-dns.com address=2606:4700:4700::1111
/ip dns static add name=cloudflare-dns.com address=2606:4700:4700::1001
```

## 4. Habilitar DoH de Cloudflare, permitir peticiones LAN y limpiar servidores tradicionales
```routeros
/ip dns set use-doh-server=https://cloudflare-dns.com/dns-query verify-doh-cert=yes allow-remote-requests=yes servers=""
```

## 5. Limpiar cache DNS para aplicar los cambios inmediatamente
```routeros
/ip dns cache flush
```
