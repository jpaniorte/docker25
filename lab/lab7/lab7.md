# Lab 7: Play with Docker Build

## Ejercicio 1

[Leer documentación](https://gitlab.com/curso_docker_2401/docs#como-trabajar-con-los-ejemplos) 

## Ejercicio 2: "Hello Dockerfile" 
**Objetivo**: Crear un Dockerfile básico que use una imagen base y muestre un mensaje en pantalla.

Instrucciones:

1. Crea un archivo llamado Dockerfile.
2. Usa una imagen base de alpine.
3. Configura el contenedor para ejecutar el comando echo "Hola, Docker!".
4. Construye la imagen con:
```
docker build -t mi-primera-imagen .
```
5. Ejecuta el contenedor
```
docker run --rm mi-primera-imagen
```
6. verifica la salida:
```
Hola, Docker!
```

## Ejercicio 3:  "Servidor Web Estático" 
**Objetivo**: Crear un contenedor con nginx que sirva una página HTML.

Instrucciones:

1. Crea un archivo index.html con cualquier contenido.

2. Escribe un Dockerfile que:

- Use la imagen base nginx:alpine.
- Copie index.html en /usr/share/nginx/html/index.html.

3. Construye la imagen y levanta el contenedor con:
```
docker build -t mi-servidor .
docker run -d -p 8080:80 mi-servidor
```
4. Verifica que el servidor funciona
```
curl -vk http://localhost:8080
```

## Ejercicio 4: "Aplicación Python en Docker" 
**Objetivo**: Crear un contenedor que ejecute un script en Python.

Instrucciones:

1. Crea un archivo app.py con este código:
```
print("¡Hola desde Docker y Python!")
```

2. Crea un Dockerfile que:

- Use python:3.9 como imagen base.
- Copie app.py en el contenedor.

3. Ejecute el script automáticamente: `python /app.py`
4. Construye y ejecuta el contenedor para ver la salida del script.


## Ejercicio 5: "Aplicación Node.js con Dependencias" 
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
- Copie los archivos al contenedor.
- Instale dependencias (npm install express).
- Exponga el puerto 3000.
- Ejecute node server.js.

3. Construye y ejecuta el contenedor, luego accede a http://localhost:3000.

## Ejercicio 6: "Imagen Optimizada con Multi-Stage Build" 
**Objetivo**: Reducir el tamaño de una imagen Node.js usando Multi-Stage Builds.

Modifica el ejercicio anterior para que:

- Use un primer stage basado en node:18 para instalar dependencias.
- Copie solo los archivos necesarios a un segundo stage con node:18-alpine.
- Use CMD en lugar de ENTRYPOINT.
- Construye y ejecuta la imagen.

Compara el tamaño de la imagen optimizada con la versión sin multi-stage.


