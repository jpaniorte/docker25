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
- [**restart:** Restart one or more containers](#docker-restart)
- [**stop:** Stop one or more running containers](#docker-stop)
- [**start:** Start one or more stopped containers](#docker-start)
- [**rm:** Remove one or more containers](#docker-rm)

### [Imágenes](#ejercicios-de-imágenes)
- [**image:** Manage images](#docker-image)
- [**commit:** Create a new image from a container's changes](#docker-commit)
- [**build:** Build an image from a Dockerfile](#docker-build)
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
### docker exec
### docker ps
### docker cp
### docker restart
### docker stop
### docker start
### docker rm

## Ejercicios de Imágenes
### docker image
### docker commit
### docker build
### docker pull
### docker push
### docker export
### docker load
### docker rmi
### docker tag
### docker trust

## Ejercicios de Redes y volúmenes
### docker network
### docker volume


