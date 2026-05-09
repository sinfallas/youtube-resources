#!/usr/bin/env bash
# Made by Sinfallas <sinfallas@yahoo.com>
# Licence: GPL-2
LC_ALL=C

if [[ "$EUID" != "0" ]]; then
	echo -e "\e[00;31mERROR: Debes ser root.\e[00m"
	exit 1
fi

echo "Este script desinstalara los drivers de nvidia incluidos en Ubuntu 26.04 e instalar los drivers compatibles con nvidia container toolkit."
echo "Presione Enter para continuar o Ctrl + C para finalizar..."
read -p "$*"

apt update
apt -y install curl gnupg2

# repositorio de nvidia
mkdir -p /etc/apt/keyrings
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/nvidia.gpg] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/ /" > /etc/apt/sources.list.d/nvidia-cuda.list
curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xA4B469963BF863CC" | gpg --dearmor | tee /etc/apt/keyrings/nvidia.gpg > /dev/null
chmod 644 /etc/apt/keyrings/*.gpg

# instalacion
apt update
apt -y install linux-nvidia linux-tools-nvidia linux-headers-nvidia linux-nvidia-7.0 linux-tools-nvidia-7.0 linux-headers-nvidia-7.0 nvidia-dkms-open nvidia-driver-open nvidia-kernel-source-open libnvidia-egl-wayland1 pkg-config xcvt xserver-xorg-core screen-resolution-extra nvidia-cuda-toolkit nvidia-firmware linux-firmware-nvidia-graphics nvidia-kernel-common libnvidia-gl libnvidia-fbc1 libnvidia-extra libnvidia-encode libnvidia-decode libnvidia-common libnvidia-cfg1 libnvidia-compute nvidia-container-toolkit nvidia-modprobe nvidia-vaapi-driver libxnvctrl0 switcheroo-control nvtop nvidia-settings

# configuracion
nvidia-ctk runtime configure --runtime=docker
nvidia-ctk system create-dev-char-symlinks --create-all
echo "# This will create /dev/char symlinks to all device nodes" > /lib/udev/rules.d/71-nvidia-dev-char.rules
echo 'ACTION=="add", DEVPATH=="/bus/pci/drivers/nvidia", RUN+="/usr/bin/nvidia-ctk system 	create-dev-char-symlinks --create-all"' >> /lib/udev/rules.d/71-nvidia-dev-char.rules
groupadd -g 143 nvidia-persistenced
useradd -c 'NVIDIA Persistence Daemon' -u 143 -g nvidia-persistenced -d '/' -s /sbin/nologin nvidia-persistenced
echo 'options nvidia "NVreg_DynamicPowerManagement=0x02"' > /etc/modprobe.d/nvidia.conf
systemctl restart docker

echo "Finalizado, se recomienda reiniciar el equipo."
