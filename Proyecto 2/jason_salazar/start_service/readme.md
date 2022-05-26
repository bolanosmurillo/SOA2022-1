# Construir imagen en Docker:
    docker build -t soa/start-service .

# Cargar imagen a minikube:
    minikube image load soa/start-service:latest

# Ver la images en minukube:
    minikube image ls

# Hacer el deployment de este servicio:
    kubectl apply -f deployment.yaml

# Ver el nuevo deployment y el pod:
    kubectl get deployments
    kubectl get pods

# Mapear el puerto del servicio para acceso local
    kubectl port-forward deployment/start-service 4001:4001


# Si se quiere obtener la ip interna de los servicios:
    kubectl -n <insert namespace> get svc

# #### Para borrar!!! ##########

# Para borrar este deployment:
    kubectl delete deployment start-service

# Para borrar el servicio:
    kubectl delete service start-service

# Borrar imagen:
    minikube image rm soa/start-service:latest

# Borra imagen en docker:
    docker rmi soa/start-service:latest
