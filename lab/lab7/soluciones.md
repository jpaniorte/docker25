## Ejercicio 2

`Dockerfile`

        FROM alpine:latest
        CMD ["echo", "Hola, Docker!"]

## Ejercicio 3

Estructura de archivos:

        /mi-servidor
        │── Dockerfile
        │── index.html

`Dockerfile`

        FROM nginx:alpine
        COPY index.html /usr/share/nginx/html/index.html
        EXPOSE 80

## Ejercicio 4

Estructura de archivos:

        /mi-python
        │── Dockerfile
        │── app.py

`Dockerfile`

        FROM python:3.9-slim
        COPY app.py /app.py
        CMD ["python", "/app.py"]

## Ejercicio 5

Estructura de archivos:

        /mi-node
        │── Dockerfile
        │── package.json
        │── server.js

`Dockerfile`

        FROM node:18
        WORKDIR /app
        COPY package.json ./
        COPY server.js ./
        RUN npm install
        EXPOSE 3000
        CMD ["node", "server.js"]

## Ejercicio 6

        FROM node:18 AS builder
        WORKDIR /app
        COPY package.json ./
        RUN npm install
        COPY server.js ./

        FROM node:18-alpine
        WORKDIR /app
        COPY --from=builder /app .
        EXPOSE 3000
        CMD ["node", "server.js"]

