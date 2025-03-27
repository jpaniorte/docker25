# Laboratorio 2: Play with Docker

En el siguiente laboratorio, vamos a practicar los siguientes comandos de Docker CLI:

### [Administración](#ejercicios-de-administración)
- [**info:** Display system-wide information](#docker-info)
- [**version:** Show the Docker version information](#docker-version)
- [**system:** Manage Docker](#docker-system)
- [**events:** Get real time events from the server](#docker-events)
- [**inspect:** Return low-level information on Docker objects](#docker-inspect)
- [**logs:** Fetch the logs of a container](#docker-logs)
- [**port:** List port mappings or a specific mapping for the container](#docker-port)
- [**stats:** Display a live stream of container(s) resource usage statistics](#docker-stats)
- [**top:** Display the running processes of a container](#docker-top)

### [Contenedores](#ejercicios-de-contenedores)
- [**run:** Create and run a new container from an image](#docker-run)
- [**exec:** Execute a command in a running container](#docker-exec)
- [**ps:** List containers](#docker-ps)
- [**cp:** Copy files/folders between a container and the local filesystem](#docker-cp)
- [**rm:** Remove one or more containers](#docker-rm)

### [Imágenes](#ejercicios-de-imágenes)
- [**image:** Manage images](#docker-image)
- [**commit:** Create a new image from a container's changes](#docker-commit)
- [**pull:** Download an image from a registry](#docker-pull)
- [**push:** Upload an image to a registry](#docker-push)
- [**export:** Export a container's filesystem as a tar archive](#docker-export)
- [**load:** Load an image from a tar archive or STDIN](#docker-load)
- [**rmi:** Remove one or more images](#docker-rmi)
- [**tag:** Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE](#docker-tag)
- [**trust:** Manage trust on Docker images](#docker-trust)

### [Redes y volúmenes](#ejercicios-de-redes-y-volúmenes)
- [**network:** Manage networks](#docker-network)
- [**volume:** Manage volumes](#docker-volume)
---

## Ejercicios de Administración

### docker info
- Ejercicio: Explorando la Información del Sistema Docker

**Objetivo:** Comprender qué información proporciona docker info y cómo interpretar sus datos.

Escribe el siguiente comando y ejecútalo:

    docker info

Analiza la salida y responde las siguientes preguntas:

- ¿Cuál es la versión del servidor de Docker que estás utilizando?
- ¿Cuántos contenedores están en ejecución, detenidos y creados?
- ¿Qué tipo de almacenamiento (Storage Driver) está usando Docker en tu sistema?

### docker version

- Ejercicio: Identificando la Versión de Docker y sus Componentes

**Objetivo**: Comprender la diferencia entre la versión del cliente y del servidor de Docker, y cómo verificar compatibilidad entre versiones.

Abre una terminal y ejecuta el siguiente comando:

    docker version

Analiza la salida y responde las siguientes preguntas:

- ¿Cuál es la versión del cliente de Docker instalada en tu sistema?
- ¿Cuál es la versión del servidor (Engine)?
- ¿Las versiones del cliente y del servidor coinciden? Si no, ¿qué podría significar esto?
- ¿Qué API version está utilizando tu Docker Engine?

### docker system

- Ejercicio: Ver información general del sistema Docker

**Objetivo**: Comprender el propósito de docker system y cómo usar sus subcomandos para gestionar recursos de Docker.

Ejecuta el siguiente comando y analiza su salida:

    docker system info

¿En qué se diferencia esta salida de docker info? ¿Qué información adicional encuentras aquí?

Comprobar el uso de espacio en disco. Ejecuta:

    docker system df

Responde las siguientes preguntas:

- ¿Cuánto espacio ocupan actualmente las imágenes en tu sistema?
- ¿Cuántos contenedores tienes creados, en ejecución y detenidos?
- ¿Cuánto espacio ocupan los volúmenes?

Liberar espacio en Docker. Si quieres eliminar datos innecesarios, ejecuta:

    docker system prune

- ¿Qué elementos ha eliminado Docker?
- ¿Qué diferencia hay entre docker system prune y docker system prune -a? Antes de ejecutar docker system prune -a, intenta predecir qué impacto tendrá en tu sistema.


Ejecuta docker `system df -v` y explica la diferencia con docker system df. ¿Por qué es importante revisar el uso de disco en entornos con espacio limitado?

### docker events
- Ejercicio: Monitorizando Eventos en Docker con docker events

**Objetivo**: Comprender cómo docker events permite monitorear en tiempo real las acciones realizadas en Docker.

Ejecutar docker events y observar los cambios en tiempo real. Abre una terminal y ejecuta el siguiente comando:

    docker events

Deja la terminal abierta y en otra terminal realiza las siguientes acciones:

Crea un contenedor con nginx:

    docker run -d --name test-nginx nginx
Detén el contenedor:

    docker stop test-nginx
Elimina el contenedor:

    docker rm test-nginx

- Observa la terminal donde ejecutaste docker events. ¿Qué tipo de eventos aparecen? ¿Qué información muestra cada evento?

Filtrando eventos específicos. En lugar de ver todos los eventos, filtra solo los relacionados con contenedores:

    docker events --filter 'type=container'

Repite la creación y eliminación de un contenedor. ¿La salida es más clara que sin el filtro? ¿Por qué crees que es útil este filtro?

Obteniendo eventos dentro de un rango de tiempo. Para ver eventos ocurridos en los últimos 30 segundos, usa:

    docker events --since 30s

- ¿Aparecen los eventos de los contenedores que creaste y eliminaste antes?

Usa docker events para monitorear imágenes en lugar de contenedores:

    docker events --filter 'type=image'

Descarga una imagen nueva `docker pull apache` y observa qué eventos aparecen.

### docker inspect

- Ejercicio: Inspeccionando Objetos en Docker con docker inspect

**Objetivo**: Comprender cómo docker inspect permite obtener información detallada de contenedores, imágenes, volúmenes y redes en Docker.

Crea un contenedor basado en la imagen nginx:

    docker run -d --name mi_nginx nginx

Inspecciona el contenedor con:

    docker inspect mi_nginx

Analiza la salida y responde:

- ¿Cuál es la dirección IP asignada al contenedor?
- ¿Qué puerto está expuesto?
- ¿Cuál es la ruta donde se almacena el sistema de archivos del contenedor en el host?

Filtrar Información con --format. La salida de docker inspect es extensa. Usa el formato JSON para extraer información específica:

Obtén solo la dirección IP del contenedor:

    docker inspect --format '{{ .NetworkSettings.IPAddress }}' mi_nginx

Encuentra el estado del contenedor (running, stopped, etc.):

    docker inspect --format '{{ .State.Status }}' mi_nginx

Inspeccionar una Imagen de Docker

    docker inspect nginx

- ¿Cuál es el ID de la imagen?
- ¿Qué capas (Layers) componen la imagen?

Crea un volumen en Docker:

    docker volume create mi_volumen

Inspecciona su información:

    docker inspect mi_volumen

¿Dónde está almacenado el volumen en el host?

Inspeccionar una Red de Docker. Lista las redes disponibles en tu sistema:

    docker network ls

Inspecciona la red bridge:

    docker inspect bridge

¿Cuántos contenedores están conectados a esta red?

### docker logs

- Ejercicio: Analizando Registros de Contenedores con docker logs

**Objetivo**: Comprender cómo docker logs permite visualizar la salida de los contenedores en ejecución y usar opciones para filtrar información útil.

Ver los Logs de un Contenedor. Inicia un contenedor basado en nginx:

    docker run -d --name mi_nginx nginx

Verifica su estado:

    docker ps

Muestra los registros del contenedor:

    docker logs mi_nginx

- ¿Aparece alguna salida en los logs? ¿Por qué?

Inspeccionar los Logs en Tiempo Real. Inicia un contenedor que genere salida en los logs:

    docker run -d --name mi_app busybox sh -c "while true; do echo 'Hola Docker'; sleep 2; done"

Observa los logs en tiempo real con -f (follow):

    docker logs -f mi_app

Abre otra terminal y detén el contenedor:

    docker stop mi_app

- ¿Qué ocurrió en la terminal donde estabas viendo los logs?

Mostrar Solo las Últimas Líneas de los Logs. Reinicia el contenedor que genera logs:

    docker start mi_app

Muestra solo las últimas 5 líneas del log:

    docker logs --tail 5 mi_app

- ¿Por qué puede ser útil esta opción?

Ver Logs con Marca de Tiempo. Ejecuta el siguiente comando:

    docker logs --timestamps mi_app

- ¿Cómo te ayuda a interpretar los eventos dentro del contenedor?

Filtrar Logs por Fecha y Hora. Usa docker logs --since 10s para ver solo los eventos de los últimos 10 segundos:

    docker logs --since 10s mi_app

- ¿Cómo podrías usar esto para depurar errores en una aplicación en producción?

### docker port

- Ejercicio: Identificando Puertos Expuestos con docker port

**Objetivo**: Comprender cómo docker port permite verificar qué puertos de un contenedor están mapeados en el host.

Crear un Contenedor con un Puerto Expuesto. Inicia un contenedor de nginx y expón el puerto 8080 en el host:

    docker run -d --name mi_nginx -p 8080:80 nginx

Lista los contenedores en ejecución:

    docker ps

Observa la columna PORTS. ¿Qué información muestra?

Usar docker port para Ver los Puertos Mapeados. Ejecuta el siguiente comando para ver los puertos expuestos del contenedor:

    docker port mi_nginx

- ¿Cuál es el puerto interno del contenedor?
- ¿Cuál es el puerto del host donde está mapeado?

Probar la Conectividad al Contenedor. Abre un navegador y accede a:

    http://localhost:8080

- ¿Se muestra la página de inicio de nginx?

Si el puerto 8080 ya estaba en uso, intenta ejecutar el contenedor con otro puerto:

    docker run -d --name otro_nginx -p 9090:80 nginx

Usa `docker port otro_nginx` para verificar la nueva asignación.

Comprobar Puertos de un Contenedor que NO los Expone. Ejecuta un contenedor de alpine sin exponer puertos:

    docker run -d --name mi_alpine alpine sleep 1000

Intenta ejecutar:

    docker port mi_alpine

- ¿Qué resultado obtienes? ¿Por qué?

### docker stats
- Ejercicio: Monitorizando el Uso de Recursos con docker stats

**Objetivo**: Comprender cómo docker stats permite visualizar en tiempo real el consumo de CPU, memoria, red y otros recursos de los contenedores en ejecución.

Iniciar un Contenedor y Observar su Consumo de Recursos. Ejecuta un contenedor de nginx:

    docker run -d --name mi_nginx nginx

Usa docker stats para ver el consumo de recursos:

    docker stats

Observa la salida y responde:

- ¿Cuánto CPU y memoria está usando mi_nginx?
- ¿Está generando tráfico de red?

Ejecutar un Contenedor que Consuma Recursos. Lanza un contenedor de stress para generar carga en la CPU y la memoria:

    docker run -d --name estresado --rm progrium/stress --cpu 2 --vm 2 --vm-bytes 100M

Vuelve a ejecutar docker stats. ¿Notas un aumento en el uso de CPU y memoria?

Detén el contenedor para liberar los recursos:

    docker stop estresado

Monitorizar un Contenedor Específico. En lugar de ver todos los contenedores, muestra solo los recursos de mi_nginx:

    docker stats mi_nginx

- ¿Es más fácil interpretar la información con un solo contenedor?

Limitar el Uso de Recursos y Comparar Resultados. Crea un contenedor nginx con un límite de CPU y memoria:

    docker run -d --name nginx_limitado --memory=100m --cpus=0.5 nginx

Ejecuta docker stats nginx_limitado. ¿Está usando más CPU o memoria que el contenedor sin restricciones? ¿Qué pasa si intentas aumentar la carga en un contenedor con límites? (prueba con el contenedor `estresado`)

### docker top

- Ejercicio: Visualizando Procesos en un Contenedor con docker top

**Objetivo**: Comprender cómo docker top permite inspeccionar los procesos en ejecución dentro de un contenedor de Docker.

Iniciar un Contenedor y Ver sus Procesos. Ejecuta un contenedor basado en nginx:

    docker run -d --name mi_nginx nginx

Lista los procesos en ejecución dentro del contenedor:

    docker top mi_nginx

Observa la salida y responde: ¿Qué proceso principal está ejecutando el contenedor? ¿Cuál es su PID (Process ID) dentro del contenedor y en el host?

Comparar con ps aux en el Host. Usa ps aux en el host para buscar el proceso de nginx:

    ps aux | grep nginx

- ¿Coinciden los PIDs mostrados en docker top con los del host?

Ejecutar un Contenedor con un Proceso Interactivo. Lanza un contenedor basado en ubuntu en modo interactivo:

    docker run -d --name mi_ubuntu ubuntu sleep 1000

Usa docker top para ver qué proceso se está ejecutando:

    docker top mi_ubuntu

- ¿Cuál es el único proceso que aparece?

Comparar docker top con docker exec. Accede al contenedor con docker exec:

    docker exec -it mi_ubuntu bash

Dentro del contenedor, ejecuta:

    ps aux

- ¿Notas alguna diferencia con la salida de docker top?

## Ejercicios de Contenedores

### docker run

#### Ejercicio 1
Diferencia entre -d y -it en docker run

**Objetivo**: Comprender la diferencia entre ejecutar un contenedor en modo detached (-d) y en modo interactivo (-it).

Paso 1: Ejecutar un contenedor en modo detached (-d). Inicia un contenedor de nginx en segundo plano:

    docker run -d --name nginx_detached nginx

Comprueba si está corriendo:

    docker ps

Intenta interactuar con él usando docker exec:

    docker exec -it nginx_detached bash

En otra terminal, muestra los procesos del contenedor haciendo uso de [docker top](#docker-top)

Paso 2: Ejecutar un contenedor en modo interactivo (-it). Inicia un contenedor de ubuntu en modo interactivo:

    docker run -it --name ubuntu_interactivo ubuntu bash

Observa que ahora tienes acceso directo a la terminal del contenedor. Escribe cualquier comando, por ejemplo:

    ls /

En otra terminal, muestra nuevamente los procesos del contenedor.


Preguntas:
- ¿Qué diferencia notaste entre los dos modos de ejecución?
- ¿Qué sucede si intentas iniciar sesión en el contenedor de nginx con `docker exec -it nginx_detached bash`?

#### Ejercicio 2

Ejecutar un Contenedor de Base de Datos con Variables de Entorno

**Objetivo**: Aprender a configurar un contenedor de base de datos pasando credenciales mediante variables de entorno.

Paso 1: Iniciar un Contenedor de MySQL. Ejecuta el siguiente comando:

    docker run -d --name mi_mysql \
      -e MYSQL_ROOT_PASSWORD=secreto \
      -e MYSQL_DATABASE=mi_base \
      -e MYSQL_USER=usuario \
      -e MYSQL_PASSWORD=clave123 \
      -p 3306:3306 \
      mysql:latest

Paso 2: Conectar a la Base de Datos. Usa otro contenedor de MySQL para conectarte:

    docker run -it --rm --network host mysql mysql -h127.0.0.1 -uusuario -pclave123 mi_base

Una vez dentro, verifica que la base de datos se ha creado:

    SHOW DATABASES;

Crea una tabla y agrega datos:

    CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50));
    INSERT INTO clientes (nombre) VALUES ('Juan'), ('Ana');
    SELECT * FROM clientes;

Preguntas:
- ¿Qué ventaja tiene usar variables de entorno en docker run para configurar la base de datos? ¿Te parece seguro?
- ¿Cómo podrías persistir los datos de MySQL usando un volumen en lugar de depender del contenedor?

### docker exec

**Objetivo**: Aprender a utilizar docker exec para ejecutar comandos dentro de un contenedor en ejecución sin necesidad de detenerlo o reiniciarlo.

Iniciar un Contenedor en Segundo Plano. Ejecuta un contenedor basado en nginx:

    docker run -d --name mi_nginx nginx

Verifica que el contenedor está corriendo:

    docker ps

Ejecutar un Comando en el Contenedor con docker exec. Lista los archivos en el directorio raíz del contenedor:

    docker exec mi_nginx ls /

Muestra los procesos en ejecución dentro del contenedor:

    docker exec mi_nginx ps aux

Acceder a una Terminal Interactiva en el Contenedor. Abre una sesión interactiva dentro del contenedor con bash:

    docker exec -it mi_nginx bash

Una vez dentro, explora el sistema de archivos con comandos como:

    ls /usr/share/nginx/html
    cat /etc/nginx/nginx.conf

Para salir, usa el comando:

    exit

### docker ps

**Objetivo**: Aprender a usar `docker ps` para listar los contenedores en ejecución y entender la información proporcionada por este comando.

Ejecutar Varios Contenedores. Inicia dos contenedores: uno basado en nginx y otro en ubuntu.

    docker run -d --name contenedor_nginx nginx
    docker run -d --name contenedor_ubuntu ubuntu sleep 100000

Verifica que ambos contenedores están en ejecución:

    docker ps

Analizar la Salida de docker ps. ¿Qué información se muestra para cada contenedor?

Ahora, ejecuta el siguiente comando para listar todos los contenedores, incluidos los detenidos:

    docker ps -a

Detén uno de los contenedores:

    docker stop contenedor_ubuntu

Vuelve a ejecutar docker ps -a y observa cómo cambia la información sobre el contenedor detenido.

Usa el comando docker ps para filtrar contenedores basados en una condición. Por ejemplo, para ver solo el contenedor que usa nginx:

    docker ps --filter "name=contenedor_nginx"

También puedes ver los contenedores en ejecución que expongan puertos. Por ejemplo, para ver todos los contenedores con puertos expuestos:

    docker ps --filter "publish=80"

### docker cp

**Objetivo**: Aprender a usar docker cp para copiar archivos entre el sistema de archivos del contenedor y el sistema de archivos del host.

Crea un archivo de texto en tu máquina local:

    echo "Contenido original en el archivo del host" > hola_host.txt

Inicia un contenedor basado en nginx:

    docker run -d --name contenedor_nginx nginx

Copia el archivo hola_host.txt desde el host al contenedor:

    docker cp hola_host.txt contenedor_nginx:/usr/share/nginx/html/hola_host.txt

Verifica que el archivo ha sido copiado al contenedor accediendo a su sistema de archivos:

    docker exec contenedor_nginx cat /usr/share/nginx/html/hola_host.txt

Ahora, crea un archivo dentro del contenedor:

    docker exec contenedor_nginx bash -c 'echo "Contenido original en el archivo del contenedor" > /usr/share/nginx/html/hola_contenedor.txt'

Copia el archivo hola_contenedor.txt desde el contenedor al host:

    docker cp contenedor_nginx:/usr/share/nginx/html/hola_contenedor.txt .

Verifica que el archivo ha sido copiado al host:

    cat hola_contenedor.txt

Modifica el archivo hola_host.txt en el host, por ejemplo:

    echo "Nuevo contenido en el archivo del host" > hola_host.txt

Copia nuevamente el archivo modificado desde el host al contenedor:

    docker cp hola_host.txt contenedor_nginx:/usr/share/nginx/html/hola_host.txt

Verifica que los cambios se reflejan dentro del contenedor:

    docker exec contenedor_nginx cat /usr/share/nginx/html/hola_host.txt

### docker rm

**Objetivo**: Aprender a eliminar contenedores con docker rm y entender las diferencias entre eliminar un contenedor detenido y uno en ejecución.

Inicia un contenedor basado en nginx en segundo plano:

    docker run -d --name contenedor_nginx nginx

Verifica que el contenedor está en ejecución:

    docker ps


Detén el contenedor con docker stop:

    docker stop contenedor_nginx

Verifica que el contenedor está detenido:

    docker ps -a

Elimina el contenedor detenido con docker rm:

    docker rm contenedor_nginx

Verifica que el contenedor ha sido eliminado:

docker ps -a

Intenta Eliminar un Contenedor en Ejecución. Inicia nuevamente un contenedor nginx en segundo plano:

    docker run -d --name contenedor_nginx nginx
    docker rm contenedor_nginx
    docker rm -f contenedor_nginx

Crea y ejecuta otros dos contenedores para este ejercicio:

    docker run -d --name contenedor_ubuntu ubuntu sleep 1000
    docker run -d --name contenedor_alpine alpine sleep 1000

Elimina ambos contenedores a la vez con un solo comando:

    docker rm contenedor_ubuntu contenedor_alpine

Verifica que ambos contenedores han sido eliminados:

    docker ps -a

Usa docker ps -a para listar todos los contenedores. Elimina todos los contenedores detenidos de una vez usando un filtro:

    docker rm $(docker ps -a -q)

Verifica que los contenedores han sido eliminados:

    docker ps -a

## Ejercicios de Imágenes
### docker image

**Objetivo**: Aprender a utilizar docker image para listar, eliminar y administrar las imágenes en Docker.

Lista todas las imágenes disponibles en tu sistema:

    docker image ls

- Observa la información que se muestra, como:
- Repositorio (nombre de la imagen)
- Etiqueta (tag)
- ID de la imagen
- Tamaño
- Fecha de creación

Eliminar una Imagen con docker image rm. Primero, ejecuta un contenedor basado en nginx:

    docker run -d --name contenedor_nginx nginx

Luego, lista las imágenes disponibles nuevamente:

    docker image ls

Elimina la imagen de nginx usando su ID o nombre:

    docker image rm nginx

Si la imagen está en uso por un contenedor en ejecución o detenido, Docker te pedirá que detengas o elimines el contenedor primero. Verifica que la imagen no ha sido eliminada:

    docker image ls

Eliminar Múltiples Imágenes con docker image rm. Crea un par de contenedores de prueba usando diferentes imágenes, como nginx y alpine:

    docker run -d --name contenedor_nginx nginx
    docker run -d --name contenedor_alpine alpine sleep 1000

Verifica las imágenes disponibles:

    docker image ls

Elimina varias imágenes a la vez por nombre o ID:

    docker image rm nginx alpine

Verifica que las imágenes han sido eliminadas:

    docker image ls

Limpiar Imágenes No Usadas con docker image prune. Usa el siguiente comando para eliminar todas las imágenes no utilizadas y liberar espacio:

    docker image prune

Este comando eliminará imágenes intermedias y no etiquetadas (dangling images). Si deseas eliminar todas las imágenes no usadas, usa el flag -a:

    docker image prune -a

Verifica las imágenes restantes después de ejecutar la limpieza:

    docker image ls

### docker commit

Crea un contenedor basado en ubuntu y realiza algunos cambios dentro del contenedor:

    docker run -it --name contenedor_ubuntu ubuntu

Dentro del contenedor, instala algún paquete o realiza cambios. Por ejemplo:

    apt-get update && apt-get install -y curl
    exit

Crea una nueva imagen desde el contenedor modificado:

    docker commit contenedor_ubuntu mi_ubuntu_modificado

Verifica que la nueva imagen ha sido creada:

    docker image ls

### docker pull

Descargar una Imagen desde Docker Hub. Abre tu terminal y ejecuta el siguiente comando para descargar la imagen oficial de nginx desde Docker Hub:

    docker pull nginx

Verifica que la imagen se haya descargado correctamente listando las imágenes locales:

    docker image ls

Observa que nginx está ahora en tu lista de imágenes locales, junto con la etiqueta latest. Algunas imágenes tienen varias versiones o etiquetas. Por ejemplo, puedes descargar una versión específica de nginx, como la versión 1.19:

    docker pull nginx:1.19

Verifica que la imagen con la etiqueta 1.19 ha sido descargada:

    docker image ls

### docker push

> Nota: Se necesita cuenta en DockerHub para estos ejercicios.

**Objetivo**: Aprender a usar el comando docker push para subir imágenes locales a Docker Hub o a un registro privado.

Iniciar Sesión en Docker Hub. Antes de poder subir imágenes a Docker Hub, debes iniciar sesión en tu cuenta de Docker Hub:

    docker login

Ingresa tu nombre de usuario y contraseña de Docker Hub cuando se te solicite.

Crear una Imagen Local Personalizada. Crea un contenedor basado en ubuntu y realiza algunos cambios en él. Por ejemplo, instala curl en el contenedor:

    docker run -it --name contenedor_ubuntu ubuntu

Una vez dentro del contenedor, ejecuta el siguiente comando para instalar curl (o cualquier otro cambio que desees hacer):

    apt-get update && apt-get install -y curl

Sal del contenedor:

    exit

Crea una imagen a partir del contenedor modificado:

    docker commit contenedor_ubuntu mi_ubuntu_con_curl

Verifica que la nueva imagen fue creada:

    docker image ls

Para subir la imagen a Docker Hub, debes etiquetarla con tu nombre de usuario y el nombre del repositorio en Docker Hub. Suponiendo que tu nombre de usuario en Docker Hub es miusuario, etiquetamos la imagen:

    docker tag mi_ubuntu_con_curl miusuario/mi_ubuntu_con_curl:latest

Verifica que la imagen ha sido etiquetada correctamente:

    docker image ls

Verás que la imagen ahora tiene la etiqueta miusuario/mi_ubuntu_con_curl:latest.

Ahora, sube la imagen a tu cuenta de Docker Hub con el siguiente comando:

    docker push miusuario/mi_ubuntu_con_curl:latest

Docker comenzará a subir la imagen. Verás un progreso similar al de la descarga, pero en este caso, será la subida de las capas de la imagen.

Accede a tu cuenta de Docker Hub desde un navegador web y navega a tu perfil. Verás que la imagen miusuario/mi_ubuntu_con_curl aparece en tu lista de repositorios. También puedes usar el siguiente comando para confirmar que la imagen está disponible públicamente (si no está privada):

docker pull miusuario/mi_ubuntu_con_curl:latest

### docker export

**Objetivo**: Aprender a usar el comando docker export para exportar el sistema de archivos de un contenedor y crear un archivo tar de la imagen del contenedor.

Inicia un contenedor desde la imagen de ubuntu:

    docker run -it --name contenedor_ubuntu ubuntu

Dentro del contenedor, crea un archivo de texto llamado hola.txt en el directorio /home:

    echo "¡Hola, Docker!" > /home/hola.txt

Sal del contenedor:

    exit

Verifica que el contenedor se ha detenido y está presente:

    docker ps -a

Utiliza el comando docker export para exportar el contenedor a un archivo tar. Este comando crea una copia del sistema de archivos del contenedor (no incluye los cambios de configuración o metadatos del contenedor):

    docker export contenedor_ubuntu > contenedor_ubuntu.tar

Verifica que el archivo contenedor_ubuntu.tar se ha creado en tu directorio actual. Puedes usar el comando ls para listar los archivos:

    ls -lh contenedor_ubuntu.tar

Inspeccionar el Contenido del Archivo Exportado
Usa el comando tar para inspeccionar el contenido del archivo tar exportado:

    tar -tf contenedor_ubuntu.tar

Esto mostrará los archivos que se encuentran dentro del archivo tar, incluyendo el archivo hola.txt en el directorio /home. Ahora que tienes un archivo tar del contenedor exportado, puedes crear una nueva imagen Docker a partir de él usando el comando docker import:

    docker import contenedor_ubuntu.tar mi_imagen_ubuntu

Verifica que la nueva imagen se ha creado:

    docker image ls

Deberías ver la imagen mi_imagen_ubuntu en la lista. Crea un contenedor desde la nueva imagen mi_imagen_ubuntu y accede a él:

    docker run -it mi_imagen_ubuntu

Verifica que el archivo hola.txt sigue presente en el contenedor en el directorio /home:

    cat /home/hola.txt

Deberías ver el mensaje: ¡Hola, Docker!.

### docker load

**docker load**: Se utiliza para cargar una imagen Docker desde un archivo tar que ha sido previamente exportado mediante docker save. Qué conserva: 
- Capas de la imagen: La estructura de capas de la imagen Docker.
- Etiquetas (tags): Las etiquetas asociadas a la imagen.
- Metadatos: Todos los metadatos relacionados con la imagen, como el nombre, la versión, etc.

Se usa principalmente para transferir imágenes completas entre diferentes sistemas o para realizar un respaldo de una imagen que ya se ha creado. Es útil cuando necesitas mover imágenes Docker de una máquina a otra sin perder ninguna información relacionada con la imagen.

**docker import**: Se utiliza para crear una imagen Docker a partir de un archivo tar que contiene el sistema de archivos de un contenedor exportado, como lo hace docker export. Qué conserva: 

- Capas de la imagen: No se conservan, ya que no estás trabajando con una imagen completa, sino con el sistema de archivos plano del contenedor.
- Etiquetas (tags): No se asignan etiquetas automáticamente (aunque se puede especificar al importar).
- Metadatos: No se conservan los metadatos del contenedor original, como el historial de la imagen o las configuraciones previas (por ejemplo, variables de entorno, configuraciones de red, etc.).

Uso: Es más adecuado cuando deseas crear una nueva imagen desde el sistema de archivos de un contenedor exportado, pero no te importa perder los detalles adicionales de la imagen original.

### docker rmi

Crea un contenedor con una imagen base, como ubuntu:

    docker run -it --name contenedor_ubuntu ubuntu

Dentro del contenedor, realiza alguna modificación simple, como crear un archivo hola.txt:

    echo "¡Hola, Docker!" > /home/hola.txt

Sal del contenedor:

    exit

Crea una nueva imagen a partir de este contenedor:

    docker commit contenedor_ubuntu mi_imagen_ubuntu

Verifica que la imagen se ha creado:

    docker image ls

Deberías ver la imagen mi_imagen_ubuntu en la lista. Elimina el contenedor creado previamente:

    docker rm contenedor_ubuntu

Ahora elimina la imagen mi_imagen_ubuntu usando docker rmi:

    docker rmi mi_imagen_ubuntu

Si la imagen está en uso por un contenedor detenido, Docker no permitirá eliminarla hasta que se eliminen los contenedores asociados. Verifica que la imagen ha sido eliminada:

    docker image ls

La imagen mi_imagen_ubuntu ya no debería aparecer en la lista.

### docker tag

Vamos a etiquetar una imagen.Por ejemplo, si quieres agregar una etiqueta que represente una versión, como v1.0:

  docker tag mi_imagen_ubuntu mi_imagen_ubuntu:v1.0

Verifica que la imagen ha sido etiquetada correctamente:

    docker image ls

Ahora, deberías ver dos versiones de la misma imagen, una con la etiqueta latest (por defecto) y otra con la etiqueta v1.0.

### docker trust

**Objetivo**: Aprender a usar el comando docker trust para firmar imágenes y asegurarse de que solo las imágenes verificadas sean utilizadas en el entorno de producción. Este ejercicio te guiará a través del proceso de habilitar la firma de imágenes y usar la confianza en Docker.

1. Pre-requisitos
Antes de comenzar, asegúrate de tener una cuenta en Docker Hub y que Docker esté configurado para usar imágenes firmadas. La firma de imágenes requiere la integración con Docker Content Trust (DCT), que habilita la verificación de la firma de las imágenes.

Inicia sesión en Docker Hub desde tu terminal:

    docker login

Proporciona tu nombre de usuario y contraseña para autenticarte.

Habilitar Docker Content Trust (DCT):
Para asegurarte de que Docker firmará las imágenes y las verificará al empujarlas o tirarlas, habilita Docker Content Trust. Ejecuta el siguiente comando para habilitarlo temporalmente:

    export DOCKER_CONTENT_TRUST=1

Esto asegura que Docker verifique las firmas antes de permitir la acción de push o pull de imágenes.

2. Crear una Imagen para Firmar
Crea una imagen Docker de ejemplo, por ejemplo, una imagen basada en ubuntu:

    docker run -it --name contenedor_ubuntu ubuntu

Realiza alguna modificación dentro del contenedor, como crear un archivo de texto:

    echo "¡Hola, Docker Trust!" > /home/hola.txt

Sal del contenedor:

    exit

Crea una nueva imagen a partir de este contenedor:

    docker commit contenedor_ubuntu mi_imagen_ubuntu

Verifica que la imagen se haya creado correctamente:

    docker image ls

Deberías ver la imagen mi_imagen_ubuntu en la lista.

3. Habilitar y Firmar la Imagen con docker trust
Para poder firmar una imagen, es necesario tener una clave pública en Docker Hub. Si no tienes una, Docker generará una clave para ti cuando uses el comando docker trust por primera vez. Primero, asegúrate de que tu cuenta de Docker Hub esté configurada para usar firmas (esto se hace automáticamente al configurar docker trust).

Firma la imagen usando docker trust y sube la imagen a Docker Hub. Por ejemplo, si tu nombre de usuario en Docker Hub es miusuario, etiqueta la imagen:

    docker tag mi_imagen_ubuntu miusuario/mi_imagen_ubuntu:v1.0

Ahora firma la imagen usando el comando docker trust sign:

    docker trust sign miusuario/mi_imagen_ubuntu:v1.0

Durante el proceso, Docker te pedirá que introduzcas la clave privada (si no tienes una ya configurada, se generará automáticamente). Verifica que la imagen ha sido firmada:

    docker trust inspect miusuario/mi_imagen_ubuntu:v1.0

Deberías ver información sobre la firma, como el "signer" (firma) asociada con la imagen.

4. Subir la Imagen Firmada a Docker Hub
Sube la imagen firmada a Docker Hub para que esté disponible para otros usuarios (o para ti en otros entornos):

    docker push miusuario/mi_imagen_ubuntu:v1.0

La imagen será subida junto con la firma.

5. Verificación de Firmas al Descargar Imágenes
Ahora, prueba a descargar la imagen desde Docker Hub en una máquina diferente o en el mismo entorno con DOCKER_CONTENT_TRUST=1 habilitado:

    docker pull miusuario/mi_imagen_ubuntu:v1.0

Docker verificará automáticamente si la imagen ha sido firmada antes de permitir su descarga.

6. Eliminar Firmas
Si deseas eliminar la firma de una imagen, puedes usar el siguiente comando:

Eliminar la firma de la imagen firmada:

    docker trust remove miusuario/mi_imagen_ubuntu:v1.0

Verifica que la firma ha sido eliminada:

    docker trust inspect miusuario/mi_imagen_ubuntu:v1.0

Ya no debería aparecer la firma asociada a la imagen.

## Ejercicios de Redes y volúmenes
### docker network

**Objetivo**: Aprender a crear y utilizar redes personalizadas en Docker para permitir la comunicación entre contenedores. También aprenderás a resolver nombres de contenedor a direcciones IP utilizando Docker DNS.

Crea una red personalizada de tipo bridge para que los contenedores puedan comunicarse entre sí:

    docker network create --driver bridge mi_red

Verifica que la red ha sido creada correctamente:

    docker network ls

Deberías ver mi_red en la lista de redes disponibles.

Crea el primer contenedor (contenedor_1) y conéctalo a la red mi_red:

    docker run -d --name contenedor_1 --network mi_red ubuntu sleep 1000

Este comando ejecutará un contenedor de Ubuntu y lo conectará a la red mi_red. El contenedor se ejecutará en segundo plano con el comando sleep 1000 para que permanezca activo.

Crea el segundo contenedor (contenedor_2) y conéctalo también a la misma red mi_red:

    docker run -d --name contenedor_2 --network mi_red ubuntu sleep 1000

De nuevo, este contenedor de Ubuntu se conecta a mi_red y permanecerá activo. Ahora, accede al primer contenedor (contenedor_1):

    docker exec -it contenedor_1 bash

Dentro del contenedor contenedor_1, intenta hacer ping al segundo contenedor (contenedor_2) usando el nombre del contenedor:

    ping contenedor_2

Docker utiliza su sistema de resolución de nombres basado en DNS para resolver el nombre del contenedor contenedor_2 y devolver la IP del contenedor. Si todo está correctamente configurado, deberías ver respuestas de ping, indicando que los contenedores están conectados correctamente.

### docker volume

#### Ejercicio 1: Usar Docker Volumes para Persistir Datos Entre Contenedores
Objetivo: Aprender a usar volúmenes de Docker para almacenar datos de manera persistente y poder compartirlos entre contenedores.

1. Crear un Volumen Docker
Crea un volumen Docker con el nombre mi_volumen:

    docker volume create mi_volumen

Verifica que el volumen ha sido creado:

    docker volume ls

2. Montar un Volumen en un Contenedor
Crea un contenedor y monta el volumen mi_volumen en el directorio /data dentro del contenedor:

    docker run -d --name contenedor_1 -v mi_volumen:/data ubuntu sleep 1000

Este contenedor ejecutará Ubuntu y montará el volumen mi_volumen en /data. El contenedor se ejecutará en segundo plano para que pueda interactuar con él después. Accede al contenedor contenedor_1 y crea un archivo dentro del directorio montado /data:

    docker exec -it contenedor_1 bash
    cd /data
    echo "Este es un archivo persistente" > archivo.txt

Ahora el archivo archivo.txt se encuentra en el volumen mi_volumen.

3. Crear un Segundo Contenedor que Acceda al Volumen
Crea un segundo contenedor (contenedor_2) y monta el mismo volumen mi_volumen en el directorio /data dentro del contenedor:

    docker run -d --name contenedor_2 -v mi_volumen:/data ubuntu sleep 1000

Accede al segundo contenedor (contenedor_2) y verifica que el archivo archivo.txt creado en el primer contenedor está disponible:

    docker exec -it contenedor_2 bash
    cd /data
    cat archivo.txt

Deberías ver el contenido del archivo: "Este es un archivo persistente".

#### Ejercicio 2: Usar Volúmenes Docker para Almacenar Datos de una Base de Datos
**Objetivo**: Aprender a usar volúmenes Docker para almacenar datos persistentes de una base de datos (por ejemplo, MySQL), de modo que los datos no se pierdan cuando el contenedor se reinicie o se elimine.

1. Crear un Volumen para la Base de Datos
Crea un volumen para almacenar los datos de la base de datos:

    docker volume create volumen_db

2. Crear un Contenedor de Base de Datos MySQL
Crea un contenedor de MySQL y monta el volumen volumen_db en el directorio /var/lib/mysql, donde MySQL almacena los datos:

    docker run -d --name mysql_db -e MYSQL_ROOT_PASSWORD=root -v volumen_db:/var/lib/mysql mysql:5.7

Verifica que el contenedor de MySQL esté funcionando:

    docker ps

3. Conectarse al Contenedor de MySQL
Accede al contenedor de MySQL para interactuar con la base de datos:

    docker exec -it mysql_db mysql -u root -p

Ingresa la contraseña root cuando se te solicite. Crea una base de datos dentro del contenedor MySQL:

    CREATE DATABASE mi_base_de_datos;

Agrega una tabla a la base de datos y agrega algunos datos:

    USE mi_base_de_datos;
    CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255));
    INSERT INTO usuarios (nombre) VALUES ('Juan'), ('Pedro');

4. Verificar la Persistencia de los Datos
Elimina el contenedor de MySQL para probar si los datos persisten:

    docker rm -f mysql_db

Vuelve a crear el contenedor de MySQL con el volumen volumen_db:

    docker run -d --name mysql_db -e MYSQL_ROOT_PASSWORD=root -v volumen_db:/var/lib/mysql mysql:5.7

Conéctate al nuevo contenedor y verifica que la base de datos y los datos siguen existiendo:

    docker exec -it mysql_db mysql -u root -p
    USE mi_base_de_datos;
    SELECT * FROM usuarios;
Los datos que insertaste previamente deberían estar presentes.

#### Ejercicio 3: Usar Volúmenes Docker con Directorios Locales (Bind Mount)

**Objetivo**: Aprender a usar los "bind mounts" de Docker para montar un directorio local en el contenedor y compartir archivos directamente entre el host y el contenedor.

1. Crear un Directorio Local
Crea un directorio local en tu máquina para almacenar los archivos del contenedor:

    mkdir /tmp/mi_directorio

2. Crear un Contenedor y Montar el Directorio Local
Crea un contenedor de Ubuntu y monta el directorio /tmp/mi_directorio en el contenedor en el directorio /data:

    docker run -d --name contenedor_bind -v /tmp/mi_directorio:/data ubuntu sleep 1000

3. Agregar un Archivo al Directorio Local
En el host (fuera del contenedor), crea un archivo en el directorio /tmp/mi_directorio:

    echo "Archivo en el directorio local" > /tmp/mi_directorio/archivo.txt

Accede al contenedor contenedor_bind y verifica que el archivo esté disponible en el directorio /data:

    docker exec -it contenedor_bind bash
    cd /data
    cat archivo.txt

Deberías ver el contenido del archivo: "Archivo en el directorio local".
