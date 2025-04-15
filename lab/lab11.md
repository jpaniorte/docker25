# Lab 11: Secret managment

La gestión segura de secretos es un componente crucial de la seguridad. Hay que evitar configurar los contenedores utilizando variables de entorno puesto que éstas son visibles en texto plano desde fuera del contenedor:

```
$ docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=foobar mysql:8.0
````

Puedes recuperar el valor de la variable de entorno con `docker inspect`:

        $ docker inspect mysql
        {
            Config": {
                Env": [
                    MYSQL_ROOT_PASSWORD=foobar
                ]
            }
        }

Del mismo modo, desde el interior del contenedor podemos ver su valor:

        $ docker exec -it mysql bash
        bash-4.4# echo $MYSQL_ROOT_PASSWORD
        foobar

Por último, los secretos configurados como variables de entorno también tienden a ser enviados accidentalmente a sus repositorios.

        versión: 3
        servicios:
        mysql:
            imagen: mysql:8.0
            entorno:
                - MYSQL_ROOT_PASSWORD=foobar

Durante este laboratorio, vamos a explorar la forma de manejar los secretos.

## Manejar secretos `docker build`

Paso 1: Guardamos el secreto en un fichero de texto

        echo "API_KEY=super-secreta-12345" > secret.txt

Paso 2: Modificamos el Dockerfile

        # syntax=docker/dockerfile:1.2
        FROM alpine

        # Instalar curl para probar el secreto (solo como demostración)
        RUN apk add --no-cache curl

        # Usar el secreto sin almacenarlo en la imagen
        RUN --mount=type=secret,id=api_key cat /run/secrets/api_key

        CMD ["cat", "/run/secrets/api_key"]

Paso 3: Construimos la imagen con el secreto

        docker build --secret id=api_key,src=secret.txt --progress=plain --no-cache -t test-secret  .


Paso 4: Ejecutamos la imagen y comprobamos que el secreto no existe

        docker run --rm mi-imagen

- Ventajas:
    - No se almacena en el historial de la imagen.
    - Se borra automáticamente después de la compilación.


## Desde `docker run`

Paso 1: Guardamos el secreto en un fichero de texto

        echo "API_KEY=super-secreta-12345" > secret.txt

Paso 2: Lo montamos en el contenedor

        docker run -v $(pwd)/secret.txt:/run/secrets/db_password mi-imagen

Paso 3: Accedemos desde dentro del contenedor:

        cat /run/secrets/db_password

- Ventajas:
    - No se expone en docker inspect.
    - Se puede restringir el acceso con permisos de archivos.
    - Desaparece cuando el contenedor se apaga.


## Manejar secretos con Docker Swarm

> ejecutar `docker swarm init` para iniciar el nodo de Swarm

Paso 1: Creamos el secreto

        echo "my_super_secret_password" | docker secret create my_secret -

Podemos listar los secretos con el comando:

        docker secret ls

Y podemos inspeccionarlo:

        docker secret inspect my_secret
        [
            {
                "ID": "tz51xu25rz2j012asa16i7290",
                "Version": {
                    "Index": 11
                },
                "CreatedAt": "2025-03-31T15:48:29.927309735Z",
                "UpdatedAt": "2025-03-31T15:48:29.927309735Z",
                "Spec": {
                    "Name": "my_secret",
                    "Labels": {}
                }
            }
        ]
Paso 2: Utilizar el password con docker compose

```yaml
---
version: '3.8'
services:
  myapp:
    image: ubuntu
    command: sleep 1000
    environment:
      - DATABASE_PASSWORD_FILE=/run/secrets/db_password
secrets:
  db_password:
    file: ./password
```