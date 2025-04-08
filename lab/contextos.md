# Contextos Docker

## Opción 1: Forma rápida

        docker context create <contexto> --docker \
            "host=ssh://ubuntu@docker25-<tu_usuario>-<contexto>.jpaniorte.com, key=/ruta/clave/privada"

## Opción 2: Forma lenta

1. Editamos el fichero `.ssh/config`

         Host <contexto>
            HostName docker25-<tu_usuario>-<contexto>.jpaniorte.com
            Port 22
            IdentityFile /ruta/clave/privada
            User ubuntu
            ControlMaster     auto 
            ControlPath       ~/.ssh/control-%C
            ControlPersist    yes

1. Crear un nuevo contexto:

        docker context create remote-docker --docker "host=ssh://<contexto>"
