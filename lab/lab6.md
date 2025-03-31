# Laboratorio 6: Inter-Container Communication

ICC (Inter Container Communication) es una opción en Docker que controla si los contenedores pueden comunicarse entre sí cuando están en la misma red.

Por defecto, Docker permite que los contenedores en una misma red bridge se comuniquen entre ellos. Esta comunicación se facilita mediante la posibilidad de usar direcciones IP privadas o nombres de contenedor dentro de la red Docker para el enrutamiento de tráfico entre contenedores.

### Requisitos previos
- Una instancia Ubuntu con Docker instalado. Puedes volver a repetir el [Laboratorio 1](./lab1.md).
- Socket daemond expuesto sin TLS
- Docker CLI configurado en la máquina local apuntando al host de Docker.
- Un usuario con permisos para ejecutar contenedores en Docker.
- https://docs.docker.com/engine/security/userns-remap/#prerequisites

### Antes de configurar ICC ...

Comunicación entre contenedores en la red predeterminada 

Levantar dos contenedores en la red predeterminada:

        docker run -d --name contenedor1 alpine sleep 3600
        docker run -d --name contenedor2 alpine sleep 3600

Intentar hacer ping entre los contenedores:

        ## Apunta la dirección IP
        docker inspect contenedor1 | grep IPAddress
        docker exec -it contenedor2 ping -c 4 <IP_ADDR>

        => salida
        PING 172.17.0.2 (172.17.0.2): 56 data bytes
        64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.090 ms
        64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.063 ms


### Configuración de ICC

1. Edita el archivo de configuración del servicio Docker:

        sudo vim /lib/systemd/system/docker.service

2. modifícala para incluir icc:

        ExecStart=/usr/bin/dockerd --icc=false -H fd:// -H tcp://0.0.0.0:2375

3. Reinicia el demonio:

         sudo systemctl daemon-reload
         sudo systemctl restart docker


### Probando ICC

Volvemos a realizar la prueba anterior:

        docker start contenedor1
        docker start contenedor2

        docker inspect contenedor1 | grep IPAddress
        docker exec -it contenedor2 ping -c 4 172.17.0.2

        => salida
        --- 172.17.0.2 ping statistics ---
        4 packets transmitted, 0 packets received, 100% packet loss


Ahora probamos configurando la red:

        docker network create --driver bridge mi_red
        docker run -d --name contenedor3 --network mi_red alpine sleep 3600
        docker run -d --name contenedor4 --network mi_red alpine sleep 3600

Intentar hacer ping entre los contenedores:

        docker exec -it contenedor3 ping -c 4 contenedor4
        
        => salida
        PING 172.17.0.2 (172.17.0.2): 56 data bytes
        64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.090 ms
        64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.063 ms

