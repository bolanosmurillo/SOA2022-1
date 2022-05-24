cd rabbitmq\publisher

# Construir imagen en Docker:
    docker build . -t soa/rabbitmq-publisher:v1.0.0

# Cargar imagen a minikube:
    minikube image load soa/rabbitmq-publisher:v1.0.0

# Ver la images en minukube:
    minikube image ls

# Hacer el deployment de este servicio:
    kubectl apply -n rabbits -f deployment.yaml

# Ver el nuevo deployment y el pod:
    kubectl -n rabbits get deployments
    kubectl -n rabbits get pods

# Mapear el puerto del servicio para acceso local
    kubectl -n rabbits port-forward rabbitmq-publisher-5769bdf8b7-lpctx  80:80

# Si se quiere obtener la ip interna de los servicios:
    kubectl -n <insert namespace> get svc


# ###############Para borrar!!#
# Para borrar este deployment:
    kubectl -n rabbits delete deployment rabbitmq-publisher

# Borrar el service
    kubectl -n rabbits delete service/rabbitmq-publisher
# Borra el secret 
    kubectl -n rabbits delete secret rabbitmq-publisher
# Borrar imagen:
    minikube image rm docker.io/soa/rabbitmq-publisher:v1.0.0
