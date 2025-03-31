# Lab 5: User namespace remapping

User namespace remapping proporcionan aislamiento para los procesos en ejecución, limitando el acceso a los recursos del sistema sin las limitaciones de Docker Rootless. [Más información sobre User namespace remapping](https://www.linux.com/news/understanding-and-securing-linux-namespaces/)

Esta técnica consiste en reasignar un usuario con menos privilegios en el host Docker a los usuarios root del proceso del contenedor. Al usuario mapeado se le asigna un rango de UIDs que funcionan dentro del espacio de nombres como UIDs normales de 0 a 65536, pero no tienen privilegios en la propia máquina anfitriona.

### Requisitos previos
- Una instancia Ubuntu con Docker instalado. Puedes volver a repetir el [Laboratorio 1](./lab1.md).
- Socket daemond expuesto sin TLS
- Docker CLI configurado en la máquina local apuntando al host de Docker.
- Un usuario con permisos para ejecutar contenedores en Docker.
- https://docs.docker.com/engine/security/userns-remap/#prerequisites

### Habilitando userns-remap en el daemond

https://docs.docker.com/engine/security/userns-remap/#enable-userns-remap-on-the-daemon


### Prueba 1: Comprobación de usuario

Ejecuta un contenedor y revisa los permisos dentro y fuera del contenedor:

        docker run --rm -it alpine sh

Dentro del contenedor, verifica el usuario:

        id
        ## Salida
        uid=0(root) gid=0(root) groups=0(root)

A pesar de que dentro del contenedor aparece como root, en realidad está mapeado a un usuario sin privilegios en el host.

Para comprobarlo, abre otra terminal y encuentra el ID del contenedor:

        docker ps -a
        docker inspect <container_id> | grep "Uid"

        => Salida
        "Uid": [165536, 0, 0, 0],

Esto significa que el contenedor cree que es root, pero en realidad está ejecutándose como un usuario sin privilegios en el host.

### Prueba 2: Elevación de privilegios

Repite el laboratorio 3.

### Prueba 3: Acceso a puertos privilegiados

Verifica que Docker con User Namespace Remapping no puede enlazar puertos privilegiados (por debajo de 1024) en el host. Para ello, ejecuta un contenedor remapeado y trata de enlazar un puerto privilegiado

        docker run --rm -p 80:80 alpine nc -lk 80
        => salida esperada:
        bind: permission denied

### Diferencias entre Root, Rootful + User Namespaces y Rootless

| Feature                  | Root                         | Rootful + User Namespaces    | Rootless                          |
|--------------------------|-----------------------------|-----------------------------|----------------------------------|
| **UID dentro del contenedor** | `root` (sin restricciones) | `root` (pero mapeado)      | `1000` (usuario normal)         |
| **UID en el host**       | `root`                      | `165536+` (usuario mapeado) | `1000` (el usuario real)        |
| **Acceso a `/var/lib/docker`** | ✅ Sí (sin restricciones)  | ✅ Sí (pero limitado)      | ❌ No (usa `~/.local/share/docker`) |
| **Permisos de red**      | ✅ Usa `iptables`            | ✅ Usa `iptables`           | ⚠️ Usa `slirp4netns` (más lento) |
| **Aislamiento**          | ❌ Sin aislamiento          | ✅ Mejor que Rootful normal | ✅ Mayor seguridad total        |
| **Compatibilidad**       | ✅ Máxima                   | ✅ Alta                     | ⚠️ Algunas restricciones        |
