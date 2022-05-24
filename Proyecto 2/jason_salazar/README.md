# proyecto2soa


# Iniciar Minikube:
    minikube start
# Montar un filesystems:
    minikube mount C:/minikubevolume:/host

# Orden del deploy de servicios:
    Ver README dentro de rabbitmq\kubernetes
    Ver README dentro de rabbitmq\applications\publisher
    Ver README dentro de start_service
    Ver README dentro de image_analyzer_service
    ver README dentro de save_service

# Exponer el servicio start_service
    kubectl port-forward deployment/start-service 4001:4001    


# Comandos utilies

# Para correr un container de manera interactiva:
    docker exec -it e9d5af9b644f /bin/sh

# Para correr un pod de forma interactiva:
    kubectl exec -it <nombre del pod> -- <comando a ejecutar por ej: /bin/sh  o el comando bash> 