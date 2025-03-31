# Lab 8: Scan images with Trivy

Trivy es una herramienta de código abierto para realizar escaneos de vulnerabilidades en imágenes Docker. Detecta problemas de seguridad tanto en el sistema operativo como en las dependencias de las aplicaciones dentro de los contenedores. Para utilizar Trivy, solo necesitas instalarlo y ejecutar un simple comando para escanear una imagen.

Trivy es compatible con Docker Hub y otros registros de imágenes y proporciona un análisis detallado de vulnerabilidades, incluyendo la gravedad y las recomendaciones para mitigar los problemas encontrados.

https://trivy.dev/v0.15.0/

## Instalación 

Instala Trivy en la instancia Ubuntu Server siguiendo esta guia de instalación: https://trivy.dev/v0.15.0/installation/

## Ejercicio 1

Analiza la imagen `python:3.4-alpine`con el siguiente comando:

        trivy image python:3.4-alpine

Ahora analiza la imagen `python:3.12-alpine`:

        trivy image python:3.12-alpine

Analiza los resultados.

## Ejercicio 2

Accediendo a esta URL: https://hub.docker.com/search?type=image&badges=official&sort=pull_count&order=desc puedes observar una série de imágenes Docker de DockerHub con más descargas y Oficiales de Docker.

Escanea algunas de estas imágenes, prueba la etiqueta `latest` y algunos tags que consideres interesantes.

## Ejercicio 3

Analiza las imágenes del Laboratorio 7.