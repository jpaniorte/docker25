# Lab 9: Lint Dockerfile with Hadolint

[Hadolint](https://github.com/hadolint/hadolint) es una herramienta de análisis estático para Dockerfiles. Analiza los ficheros en busca de errores de sintaxis, buenas prácticas y posibles vulnerabilidades, proporcionando recomendaciones para optimizar las configuraciones. 

Soporta una amplia gama de reglas configurables y personalizables, lo que te permite ajustar el análisis. Se recomienda integrar Hadolint en los trabajos de CI/CD para garantizar las mejores prácticas, reducir riesgos de seguridad y mejorar la eficiencia en la construcción de contenedores.

## Instalación 

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