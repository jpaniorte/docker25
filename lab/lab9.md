# Lab 9: Lint Dockerfile with Hadolint

Hadolint es una herramienta de análisis estático para Dockerfiles que ayuda a mejorar la calidad y la seguridad de tus imágenes Docker. Analiza tus Dockerfiles en busca de errores de sintaxis, buenas prácticas y posibles vulnerabilidades, proporcionando recomendaciones para optimizar las configuraciones. Hadolint soporta una amplia gama de reglas configurables y personalizables, lo que te permite ajustar el análisis según tus necesidades. Al integrar Hadolint en tu flujo de trabajo de desarrollo, puedes asegurarte de que tus Dockerfiles sigan las mejores prácticas, reduzcan riesgos de seguridad y mejoren la eficiencia en la construcción de contenedores.

https://github.com/hadolint/hadolint

## Instalación 

En la instancia Ubuntu Server:

        wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64
        mv hadolint-Linux-x86_64 hadolint
        chmod +x hadolint
        mv hadolint /usr/local/bin

## Ejercicio 1

Analiza el siguiente Dockerfile:

        FROM ubuntu:latest
        RUN apt-get update && apt-get install -y python3 pip
        WORKDIR /app
        COPY . /app
        RUN pip install -r requirements.txt
        ENV SECRET_KEY="supersecretkey"
        EXPOSE 5000
        CMD python3 app.py

y analiza los errores.

## Ejercicio 2

Analiza los ficheros Dockerfile del laboratorio 7.