# Laboratorio 4: Docker Rootlees

El modo Rootles de Docker permite ejecutar `daemond` y los contenedores como un usuario no root previniendo ataques de escalada de privilegios desde dentro de un contenedor. Durante este laboratorio, vamos a configurar `daemond` de Docker en modo Rootless: 

Documentación:
https://docs.docker.com/engine/security/rootless/

## Antes de comenzar ...

Realizaremos una serie de pruebas sobre la instalación de Docker con root, que nos premitirán comparar posteriormente con el modo rootless.

### Prueba 1: Rendimiento
Ejecuta un contenedor simple y mide los tiempos:

        ## Prueba simple
        time docker run --rm alpine echo "Hello World"

        ## Creación de archivos
        docker run --rm -v $(pwd):/data alpine sh -c "time dd if=/dev/zero of=/data/testfile bs=1M count=500"

        ## Crear proyecto Node
        docker run --rm -w /app -v $(pwd):/app node:18 bash -c "time npx create-react-app myapp --use-npm"

### Prueba 2: Redes
Desde la instancia Ubuntu Server, comprueba la configuración de red de la red docker0:

        ip a

Ahora 

        ## Configuración de red 
        docker network create testnet
        docker run --rm --net=testnet alpine ifconfig

Revisa si la IP del contenedor pertenece a la red docker0.

### Prueba 3: Seguridad
Intenta lanzar un contenedor privilegiado e instalar un paquete con apt:

        docker run -it --privileged ubuntu bash
        apt update
        apt install nano

Muestra tu usuario en el contenddor:
        
        id
        

## Rootless

### Configura *daemond* en modo Rootless:

https://docs.docker.com/engine/security/rootless/#install

### Elevando privilegios

Vuelve a ejecutar el [lab3](./lab3.md). 

### Comparando Rootless vs Rootfull

Lanza de nuevo las pruebas anteriores y compara con los resultados obtenidos anteriormente. 

Algunas claves para comprender los resultados:

- Docker Rootfull:
    - Ejecuta contenedores con mejor rendimiento porque accede directamente a los recursos del sistema.
    - Usa iptables y bridge networking permitiendo una conectividad más rápida entre contenedores y con el host.
    - Acceso completo al sistema de archivos, permitiendo montajes y escritura sin restricciones.

- Docker Rootless:
    - Tiene mayor latencia debido a la sobrecarga de namespaces y la falta de acceso directo al kernel.
    - Usa slirp4netns para emular la interfaz de red provocando mayor latencia y menor rendimiento en transferencia de datos.
    - No permite conexiones directas a localhost sin configuraciones adicionales. 
    - Los permisos de archivos pueden ser problemáticos, ya que no tiene acceso directo a UID/GID del host.
    - No permite contenedores privilegiados (--privileged) ni ciertos flags como --net=host, lo que puede limitar algunas aplicaciones.


