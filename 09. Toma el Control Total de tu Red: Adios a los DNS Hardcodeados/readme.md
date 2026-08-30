# Toma el Control Total de tu Red: Adios a los DNS Hardcodeados

URL del video en Youtube: https://youtu.be/OrvLlU7Hibs

¿Tus Smart TVs, Chromecast o dispositivos IoT ignoran tu servidor DNS? En este video te enseño cómo usar tu router MikroTik para interceptar y redireccionar a la fuerza todo el tráfico DNS (puerto 53) y NTP (puerto 123) que intenta salir a internet.

Aprenderás a configurar reglas dst-nat en RouterOS para tomar el control absoluto de tus peticiones, mejorar tu privacidad y obligar a todos los equipos a pasar por tu DNS local o el del propio router.

Aca te dejo los comandos que debes ejecutar en tu Mikrotik:

```bash
/ip firewall nat add action=redirect chain=dstnat comment="dns udp" dst-address-type=!local dst-port=53 in-interface=lan protocol=udp
/ip firewall nat add action=redirect chain=dstnat comment="ntp udp" dst-address-type=!local dst-port=123 in-interface=lan protocol=udp
/ip firewall nat add action=redirect chain=dstnat comment="dns tcp" dst-address-type=!local dst-port=53 in-interface=lan protocol=tcp
/ip firewall nat add action=redirect chain=dstnat comment="ntp tcp" dst-address-type=!local dst-port=123 in-interface=lan protocol=tcp
```


