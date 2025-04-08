# Lab 5: User namespace remapping

User namespace remapping proporcionan aislamiento para los procesos en ejecución, limitando el acceso a los recursos del sistema sin las limitaciones de Docker Rootless. [Más información sobre User namespace remapping](https://www.linux.com/news/understanding-and-securing-linux-namespaces/)

Esta técnica consiste en reasignar un usuario con menos privilegios en el host Docker a los usuarios root del proceso del contenedor. Al usuario mapeado se le asigna un rango de UIDs que funcionan dentro del espacio de nombres como UIDs normales de 0 a 65536, pero no tienen privilegios en la propia máquina anfitriona.

## Requisitos previos
1. Accesso SSH a la instancia `docker25-<usuario>-rmap.jpaniorte.com`
2. Contexto de Docker `inseguro`, `rootless`, `rmap` y `default` definidos. [Guia para crear contextos Docker](./contextos.md)

## Instalación

Accede a través de SSH a la instancia `docker25-<usuario>-rmap.jpaniorte.com` y ejecuta los siguientes pasos:

1. Configura el repositorio Docker

        # Add Docker's official GPG key:
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc

        # Add the repository to Apt sources:
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update

2. Instalación

        sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

3. Verifica la instalación

        sudo docker run hello-world

4. Añadimos el usuario ubuntu al grupo docker en el servidor Ubuntu:

        sudo groupadd docker
        sudo usermod -aG docker $USER
        newgrp docker

5. Comprueba que puedes ejecutar comandos docker sin sudo:

        docker run hello-world

6. Creamos el usuario dockremap

        sudo useradd  dockremap

7. Configuramos el dockerd para que inicie con ese usuario

        echo '{ "userns-remap": "dockremap" }' | sudo tee /etc/docker/daemon.json
        systemctl restart docker

### Prueba 1: Comprobación de usuario

Desde el PC del laboratorio, ejecuta los siguientes comandos:

        docker context use rmap

Ejecuta el siguiente contenedor para visualizar el usuario desde dentro del contenedor:

        docker run -it --rm alpine id
     
Ejecuta los siguientes comandos para visualizar el usuario que realmente ha iniciado el contenedor:

        docker run -d --name test --rm alpine sleep 10000
        # Copia el PID del siguiente comando
        docker top test
        
        ps aux | grep <PID>
        # Analiza la primera columna.

### Prueba 2: Instalación de paqueteria

Desde una terminal en el PC del laboratorio, ejecuta y anota:

        docker context use rmap
        docker run -it --privileged ubuntu bash

- ¿Qué sucede?

        docker context use rmap
        docker run -it ubuntu bash
        apt update
        apt install nano

- ¿Puedes instalar paqueteria dentro del contenedor?

- ¿Qué conclusiones extraes? Discute y compara tus conclusiones con el resto de compañeros.

