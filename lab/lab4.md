# Laboratorio 4: Docker Rootlees

El modo Rootles de Docker permite ejecutar `daemond` y los contenedores como un usuario no root previniendo ataques de escalada de privilegios desde dentro de un contenedor. Documentación: https://docs.docker.com/engine/security/rootless/

## Requisitos previos
1. Accesso SSH a la instancia `docker25-<usuario>-rootless.jpaniorte.com`
2. Contexto de Docker `inseguro`, `rootless` y `default` definidos. [Guia para crear contextos Docker](./contextos.md)

## Paso 1: Instalación de Docker Rootless

Accede a través de SSH a la instancia `docker25-<usuario>-inseguro.jpaniorte.com` y ejecuta los siguientes pasos:

        sudo apt-get -y install uidmap 
        echo 0 | sudo tee /proc/sys/kernel/apparmor_restrict_unprivileged_userns
        curl -fsSL https://get.docker.com/rootless | sh
        vim /home/ubuntu/.bashrc
        ## Añade la siguiente línea y sal del editor
        export PATH=/home/ubuntu/bin:$PATH
        ## Prueba
        docker run hello-world

### Paso 2: Rendimiento en el contexto inseguro

Desde el PC del laboratorio, ejecuta los siguientes comandos y guarda los resultados:

        docker context use inseguro

        ## Prueba simple
        time docker run --rm alpine echo "Hello World"

        ## Creación de archivos
        docker run --rm -v /:/data alpine sh -c "time dd if=/dev/zero of=/data/testfile bs=1M count=500"

        ## Crear proyecto Node
        docker run --rm -w /app -v $(pwd):/app node:18 bash -c "time npx create-react-app myapp --use-npm"

### Paso 2: Rendimiento en el contexto default

Desde el PC del laboratorio, ejecuta los siguientes comandos y guarda los resultados:

        docker context use default

        ## Prueba simple
        time docker run --rm alpine echo "Hello World"

        ## Creación de archivos
        docker run --rm -v $(pwd):/data alpine sh -c "time dd if=/dev/zero of=/data/testfile bs=1M count=500"

        ## Crear proyecto Node
        docker run --rm -w /app -v $(pwd):/app node:18 bash -c "time npx create-react-app myapp --use-npm"

### Paso 3: Rendimiendo en el contexto Rootless

Desde el PC del laboratorio, ejecuta los siguientes comandos y guarda los resultados:

        docker context use rootless

        ## Prueba simple
        time docker run --rm alpine echo "Hello World"

        ## Creación de archivos en el home NO permitido
        docker run --rm -v $(pwd):/data alpine sh -c "time dd if=/dev/zero of=/data/testfile bs=1M count=500"

        ## Creación de archivos fuera del home
        docker run --rm -v /home/ubuntu/test:/data alpine sh -c "time dd if=/dev/zero of=/data/testfile bs=1M count=500"

        ## Crear proyecto Node
        docker run --rm -w /app -v /home/ubuntu/test:/app node:18 bash -c "time npx create-react-app myapp --use-npm"


### Paso 4: Pruebas de configuración de red

Accede a través de SSH a la instancia 

- `docker25-<usuario>-inseguro.jpaniorte.com` y ejecuta y anota los siguientes pasos:

        ip a
        exit

- `docker25-<usuario>-rootless.jpaniorte.com` y ejecuta y anota los siguientes pasos:

        ip a
        exit

Desde el PC del laboratorio, ejecuta y anota:

        docker context use rootless
        docker run --rm alpine ifconfig
        docker context use inseguro
        docker run --rm alpine ifconfig

- ¿Qué conclusiones extraes? Discute tus conclusiones con el resto de compañeros

### Prueba 3: Instalación de paqueteria

Desde una terminal en el PC del laboratorio, ejecuta y anota:

        docker context use rootless
        docker run -it --privileged ubuntu bash
        apt update
        apt install nano
        docker context use inseguro
         docker run -it --privileged ubuntu bash
        apt update
        apt install nano

- ¿Qué conclusiones extraes? Discute tus conclusiones con el resto de compañeros


### Prueba 3: Elevación de privilegios

Desde una terminal en el PC del laboratorio, ejecuta y anota:

        docker context use rootless

        docker run -it --rm --name vulnerable-container \
        --privileged \
        -v /:/host \
        ubuntu:latest bash

        ## Dentro del contenedor, ejecuta:
        cd /host
        ls -la
        chroot /host /bin/bash
        whoami


        docker context use inseguro

        docker run -it --rm --name vulnerable-container \
        --privileged \
        -v /:/host \
        ubuntu:latest bash

        ## Dentro del contenedor, ejecuta:
        cd /host
        ls -la
        chroot /host /bin/bash
        whoami

- ¿Qué conclusiones extraes? Discute tus conclusiones con el resto de compañeros

