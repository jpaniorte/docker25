# Lab 10: Docker content trust

Docker Content Trust (DCT) permite verificar la integridad y autenticidad de las imágenes de Docker mediante firmas digitales. Cuando está habilitado, solo se pueden extraer y ejecutar imágenes firmadas por fuentes de confianza ayudando a prevenir ataques de suplantación o manipulación de imágenes. 

## Prerequisitos

- export DOCKER_CONTENT_TRUST=1
- Cuenta en DockerHub o acceso a un [Registry](https://hub.docker.com/_/registry) y [Notary](https://hub.docker.com/_/notary) privado.

## Firmando mi primera imagen

Inicia sesión en DockerHub con:

        docker login

Crea una fichero Dockerfile con el siguiente contenido:

        FROM alpine:latest
        CMD ["echo", "Hello, Docker Content Trust!"]

Crea la imagen:

        docker build -t <tu-usuario>/dct-test:latest .

Cuando hagas docker push, la imagen se firmará automáticamente. Si es la primera vez que firmas una imagen, Docker te pedirá que configures una clave de firma con Notary. Debes establecer una contraseña segura para proteger la clave.

        docker push <tu-usuario>/dct-test:latest

Verifica la imagen:

        docker trust inspect --pretty <tu-usuario>/dct-test:latest

## Ejercicio: Compartir imagenes firmadas

Si deseas que otra persona pueda firmar imágenes en tu repositorio, debes agregar su clave de firma a la lista de firmantes. 

Esto se hace con:

        ## Obtener clave publica del usuario
        cat ~/.docker/trust/private/<clave>.pub

        ## Añadir clave publica a la imagen
        docker trust signer add --key <archivo-clave-publica.pem> <nombre-firmante> <tu-usuario>/dct-test:latest

Firma una imagen con la clave publica de un compañero y verifica que puede descargar esa imagen.
