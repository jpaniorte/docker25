# Lab 7: Play with Docker Build


> Importante: [Leer documentación](https://docs.docker.com/reference/dockerfile/) 

## Ejercicio 1: "Hello Dockerfile" 
**Objetivo**: Crear un Dockerfile que use una imagen base `alpine:latest` y muestre un mensaje en pantalla.

Instrucciones:

1. Crea un archivo llamado Dockerfile.
2. Usa una imagen base de alpine en la etiqueta FROM.
3. Usa la etiqueta CMD para mostrar el mensaje "Hola, Docker!".
4. Construye la imagen con:
```
docker build -t ejercicio1 .
```
5. Ejecuta el contenedor
```
docker run ejercicio1
```
6. verifica la salida:
```
Hola, Docker!
```

## Ejercicio 2: "Aplicación Python en Docker" 
**Objetivo**: Crear un contenedor que ejecute un script en Python.

Instrucciones:

1. Crea un archivo app.py con este código:
```
print("¡Hola desde Docker y Python!")
```

2. Crea un Dockerfile que:

- Use `python:3.9-slim` como imagen base.
- Espacio de trabajo: `/app`.
- Copie `app.py` en `/app`.
- Defina `python` como el comando que **siempre se va a ejecutar**.
- Defina `app.py` como el primer argumento por defecto.

3. Construye la imagen con el nombre `ejercicio4`.
4. Ejecuta el contenedor con la siguiente instrucción: `docker run ejercicio4`.
5. *opcional:* Realiza las modificaciones que consideres oportunas para que la versión de python sea una variable definida en tiempo de ejecución.
6. *opcional:* Realiza las modificaciones que consideres oportunas para que, al ejecutar `docker run ejercicio4 Juan`, muestre por pantalla: `hello world, Juan` haciendo uso de [argparse](https://docs.python.org/es/3/library/argparse.html).


## Ejercicio 3: "Aplicación Node.js con Dependencias" 
**Objetivo**: Construir una imagen Docker que ejecute una aplicación Node.js con dependencias.

Instrucciones:

1. Crea un archivo server.js con un servidor básico de Express:

`server.js`
```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('¡Hola desde Node y Docker!');
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
```
`package.json`
```
{
  "name": "mi-node-app",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```
2. Escribe un Dockerfile que:

- Use node:18 como imagen base.
- Copie los archivos necesarios para configurar e iniciar el servidor.
- Instale dependencias con `npm install`.
- Inidque la intencionalidad de exponer el puerto 3000 en tiempo de ejecución.
- El comando por defecto sea: `node server.js`.
- La imagen debe ser óptima, de tal manera que:
  - Construye la imagen con: `docker build -t ejercicio3:v1`
  - Muestra los IDs de las capas que componen la imagen:
    - Ejecuta: `docker images` y copia el id de la imagen `ejercicio3:v1`.
    - Ejecuta `docker inspect --format='{{range .RootFS.Layers}}{{println .}}{{end}}' <id_de_la_imagen>`

  - Ahora, modifica el fichero `server.js`: En la línea 5, muestra el msg: `"¡Hola desde Node y Docker v2¡"`
  - Vuelve a construir la imagen con el tag `v2`: `docker build -t ejercicio3:v2`
  - Muestra los IDs de las campas que componen la imagen `ejercicio3:v2`:
  - ¿Cuántas capas has logrado reutilizar? ¿Cuántas capas has necesitado? Compara tu salida con la de tus compañeros, 

3. Construye y ejecuta el contenedor, luego accede a http://localhost:3000.

## **OPCIONAL** Ejercicio 4: "Imagen Optimizada con Multi-Stage Build" 
**Objetivo**: Reducir el tamaño de una imagen Node.js usando Multi-Stage Builds.

Modifica el ejercicio anterior para que:

- Use un primer stage llamado `builder` basado en node:18 para instalar dependencias.
- Use un segundo stage donde únicamente copie los archivos necesarios a una imagen `node:18-slim`

Compara el tamaño de la imagen optimizada con la versión sin multi-stage.


