# Laboratorio 1: Instalación servicio Docker 

En el siguiente laboratorio realizaremos la instalación de Docker en un servidor Ubuntu Server 24.04 LTS. Esta máquina será el Docker Host para el resto de laboratorios y nos permitirá evaluar la seguridad de diferentes configuraciones de `dockerd`.

Puedes seguir [esta guía](#ubuntu-server-2404-ec2-aws) para configurar una instancia gratuita en AWS o puedes utilizar cualquier otro cloud o sistema de virtualización. Asegúrate de tener acceso SSH y el puerto 2375 abierto.

Una vez tengas acceso a la instancia, sigue los pasos de esta guía para realizar la instalación de Docker: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

Ahora, vamos a configurar Docker para escuchar conexiones remotas:

1. Edita el archivo de configuración del servicio Docker:

        sudo vim /lib/systemd/system/docker.service

2. Busca la línea que comienza con:

        ExecStart=/usr/bin/dockerd -H fd://

3. modifícala para incluir -H tcp://0.0.0.0:2375:

        ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375

Finalmente, configuraremos nuestro Docker CLI para que apunte a este nuevo Docker Host:


1. Crear un nuevo contexto:

        docker context create remote-docker --docker "host=tcp://IP_DEL_HOST_REMOTO:2375"

2. Listar los contextos disponibles:

        docker context ls

3. Cambiar al nuevo contexto:

        docker context use remote-docker

4. Para volver al host local de Docker Desktop:

        docker context use default

> Recuerda que la configuración actual de Docker es insegura. Asegúrate de cerrar el puerto 2375 o bien modifica la configuración de Docker.

## Ubuntu Server 24.04 EC2 AWS

### 1. Creación de una cuenta en AWS

1. Accede a la página principal de AWS: [https://aws.amazon.com/](https://aws.amazon.com/).
2. Haz clic en **"Create an AWS Account"**.
3. Ingresa tu dirección de correo electrónico, elige un nombre de usuario para la cuenta y establece una contraseña.
4. Selecciona el tipo de cuenta: **"Personal"**.
5. Introduce tus datos personales (nombre, dirección, número de teléfono, etc.).
6. Proporciona un método de pago (tarjeta de crédito o débito). AWS podría hacer un pequeño cargo temporal para verificar la tarjeta.
7. Verifica tu identidad introduciendo el código enviado a tu teléfono.
8. Selecciona un plan: **elige la capa gratuita (Free Tier)** para evitar cargos adicionales.
9. Accede a la consola de AWS (AWS Management Console) desde [https://console.aws.amazon.com/](https://console.aws.amazon.com/).

### 2. Configurar un límite de gasto en AWS Free Tier

Para evitar costos inesperados, puedes configurar alertas de facturación:

1. En la consola de AWS, busca y accede al servicio **Billing (Facturación)**.
2. En la barra lateral, haz clic en **Billing Preferences (Preferencias de Facturación)**.
3. Activa la opción **"Receive Free Tier Usage Alerts"** para recibir alertas sobre el uso de la capa gratuita.
4. Para establecer una alerta de gasto:
   - Ve a **Budgets (Presupuestos)** en el servicio de facturación.
   - Haz clic en **Create a Budget (Crear un presupuesto)**.
   - Elige **Cost Budget (Presupuesto de costos)** y define un límite (ej. 1€).
   - Configura una alerta para que te notifique cuando el gasto supere un porcentaje del límite definido.
   - Proporciona una dirección de correo electrónico para recibir las notificaciones.
   - Guarda los cambios.

### 3. Lanzar una instancia EC2 Free Tier con Ubuntu

1. Accede a la consola de AWS y dirígete a **EC2**.
2. En el panel de EC2, haz clic en **"Launch Instance" (Lanzar Instancia)**.
3. Asigna un nombre a la instancia (ej. "MiServidorUbuntu").
4. Selecciona una imagen del sistema operativo (AMI):
   - Haz clic en **"Ubuntu"**.
   - Elige **Ubuntu Server 24.04 LTS (Free Tier Eligible)**.
5. Selecciona el tipo de instancia:
   - Escoge **t2.micro (Free Tier Eligible)**.
6. Configura las opciones de red:
   - Asegúrate de que la instancia tenga una IP pública automática.
   - En el grupo de seguridad (Security Group), permite el tráfico **SSH (puerto 22)** para tu dirección IP y el puerto **2375**.
7. Configura el almacenamiento:
   - Usa el valor predeterminado de **8 GB de almacenamiento EBS** (dentro del Free Tier).
8. Crea o selecciona un par de claves (Key Pair) para conectarte:
   - Si no tienes uno, haz clic en **Create new key pair**.
   - Descarga el archivo `.pem` y guárdalo en un lugar seguro.
9. Revisa los detalles y haz clic en **Launch Instance**.

## 4. Conectarse a la instancia EC2 mediante SSH

1. Abre una terminal en tu computadora.
2. Navega hasta la ubicación donde guardaste la clave `.pem`.
3. Asegúrate de que el archivo tenga los permisos correctos:
   ```bash
   chmod 400 MiClave.pem
   ```
4. Conéctate a la instancia con el siguiente comando (reemplaza `your-public-ip` con la IP pública de tu instancia):
   ```bash
   ssh -i MiClave.pem ubuntu@your-public-ip
   ```
5. Una vez conectado, ya puedes empezar a usar tu servidor Ubuntu en AWS.
