## Ejercicio 1

`Dockerfile`

        FROM alpine:latest
        CMD ["echo", "Hola, Docker!"]

## Ejercicio 2

Estructura de archivos:

        /mi-python
        │── Dockerfile
        │── app.py

`Dockerfile`

        FROM python:3.9-slim
        COPY app.py /app.py
        ENTRYPOINT ["python"]
        CMD ["app.py"]

## Ejercicio 3

Estructura de archivos:

        /mi-node
        │── Dockerfile
        │── package.json
        │── server.js

`Dockerfile`

        FROM node:18
        EXPOSE 3000
        WORKDIR /app
        COPY package.json ./
        RUN npm install
        COPY server.js ./
        CMD ["node", "server.js"]

## Ejercicio 4

        FROM node:18 AS builder
        WORKDIR /app
        COPY package.json package-lock.json ./
        RUN npm install
        COPY server.js ./

        FROM node:18-slim
        WORKDIR /app
        COPY --from=builder /app/node_modules ./node_modules
        COPY --from=builder /app/server.js ./
        EXPOSE 3000
        CMD ["node", "server.js"]

