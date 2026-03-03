# 🚀 ¿Qué es Overlayroot?

Es una herramienta que permite montar un sistema de archivos de solo lectura con una capa de escritura temporal en la memoria RAM (tmpfs).

Resultado: Cualquier cambio que realices (instalar apps, borrar archivos del sistema, virus, configuraciones) desaparecerá por completo al reiniciar el equipo.

## 🛠️ Pasos de Instalación y Configuración

1. Instalación del paquete
Abre tu terminal y ejecuta:

```bash
sudo apt update && sudo apt install overlayroot -y
```

2. Configuración del modo congelado
Debemos editar el archivo de configuración principal:

```bash
sudo echo 'overlayroot_cfgdisk="disabled"' > /etc/overlayroot.conf
sudo echo 'overlayroot="tmpfs:swap=0,recurse=0,size=25%"' >> /etc/overlayroot.conf
```

3. Aplicar cambios

```bash
sudo update-initramfs -c -k all
sudo update-grub2
```

Reinicia tu sistema para que el modo congelado entre en vigor:

## 🔓 Cómo hacer cambios permanentes

Si necesitas instalar una actualización o guardar un cambio real en el disco, tienes dos opciones:

### Opción A: El modo Chroot (Recomendado)
Sin desactivar el modo congelado, puedes "entrar" a la partición real para escribir:

```bash
sudo overlayroot-chroot
```

Ahora estás en la raíz real. Haz tus cambios (ej. apt upgrade) y luego

```bash
exit
```

Al salir y reiniciar, los cambios realizados dentro del chroot se habrán guardado.


### Opción B: Desactivar Overlayroot
En el grub presiona la letra "e" para editar la entrada del grub y al final de la linea que empieza con: "Linux /boot/" coloca espacio y luego overlayroot=disabled

Reinicia el sistema presionando Ctrl + x

### Como verificar si esta funcionando

Para ver si tu particion / esta montada con overlayroot ejecuta lo siguiente:

```bash
mount | grep "on / type overlay"
```
Si no te devuelve ningun resultado el sistema **no** esta utilizando overlayroot

Para saber cuanto espacio te queda disponible en ram para usar con overlayroot ejecuta:

```bash
df -h /
```

### ⚠️ Advertencias Importantes
* Consumo de RAM: Al usar tmpfs, los archivos "temporales" que crees ocuparán espacio en tu memoria RAM. No descargues archivos gigantes mientras estés en este modo.
* Persistencia de datos: Si quieres que /home sea persistente pero / esté congelado, la configuración es más avanzada (requiere particiones separadas).
* Actualizaciones de Kernel: Se recomienda desactivar overlayroot o usar chroot para actualizaciones críticas del sistema.

### 📺 Video Tutorial
Puedes ver el procedimiento detallado en mi canal de YouTube:
[Enlace al video aquí]
