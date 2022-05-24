# Construir imagen en Docker:
    docker build -t soa/save-service .

# Cargar imagen a minikube:
    minikube image load soa/save-service:latest

# Ver la images en minukube:
    minikube image ls
   
# Hacer el deployment de este servicio:
    kubectl apply -f deployment.yaml

# Ver el nuevo deployment y el pod:
    kubectl get deployments
    kubectl get pods


# #### Para borrar!!! ##########

# Para borrar este deployment:
    kubectl delete deployment save-service

# Borrar imagen:
    minikube image rm soa/save-service:latest

# Borra imagen en docker:
    docker rmi -f soa/save-service:latest


# Todo en uno:
# Limpar todo
kubectl delete deployment save-service
# Esperar un poco a que se termine el deployment
minikube image rm soa/save-service:latest; docker rmi -f soa/save-service:latest; docker build -t soa/save-service . ; minikube image load soa/save-service:latest; kubectl apply -f deployment.yaml