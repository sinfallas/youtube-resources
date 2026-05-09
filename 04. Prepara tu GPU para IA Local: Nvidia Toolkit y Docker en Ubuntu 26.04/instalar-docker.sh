#!/usr/bin/env bash
# Made by Sinfallas <sinfallas@yahoo.com>
# Licence: GPL-2
LC_ALL=C
quienh=$(ls -l /home | awk '{print $9}' | grep -v "lost+found" | tail -n +2)

if [[ "$EUID" != "0" ]]; then
	echo -e "\e[00;31mERROR: Debes ser root.\e[00m"
	exit 1
fi

# repositorio de Docker
mkdir -p /etc/apt/keyrings
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7EA0A9C3F273FCD8" | gpg --dearmor | tee /etc/apt/keyrings/docker.gpg > /dev/null
chmod 644 /etc/apt/keyrings/*.gpg

# limpieza
apt -y remove --purge docker.io docker-compose docker-doc podman-docker docker-ctop docker-ce-rootless-extras

# instalacion
apt update
apt -y install wget tar dbus-user-session uidmap docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-buildx-plugin docker-model-plugin

$ agregar los usuario al grupo docker
groupadd docker
for j in ${quienh[@]}; do
	usermod -aG docker $j
done

echo "Finalizado."
