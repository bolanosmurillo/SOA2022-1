# Construir imagen en Docker:
    docker build -t soa/analyzer-service .

# Cargar imagen a minikube:
    minikube image load soa/analyzer-service:latest

# Ver la images en minukube:
    minikube image ls

# Habilitar el addon gcp-auth: (Creo que este no es necesario)
    minikube addons enable gcp-auth

# Cargar key para autentificacion de google:
    kubectl create secret generic pubsub-key --from-file=key.json=project1-test-346303-42cd4be9b6ef.json
    
# Hacer el deployment de este servicio:
    kubectl apply -f deployment.yaml

# Ver el nuevo deployment y el pod:
    kubectl get deployments
    kubectl get pods

# Mapear el puerto del servicio para acceso local
    kubectl port-forward deployment/analyzer-service 4000:4000

# Si se quiere obtener la ip interna de los servicios:
    kubectl -n <insert namespace> get svc

# #### Para borrar!!! ##########

# Para borrar este deployment:
    kubectl delete deployment analyzer-service
# Para borrar el servicio:
    kubectl delete service analyzer-service
# Para borra el secret:
    kubectl delete secret analyzer-service

# Borrar imagen:
    minikube image rm soa/analyzer-service:latest

# Borra imagen en docker:
    docker rmi -f soa/analyzer-service:latest



# Todo en uno:
kubectl delete deployment analyzer-service; kubectl delete service analyzer-service; kubectl delete secret analyzer-service
# Esperar a que termine el deployment
minikube image rm soa/analyzer-service:latest;  docker rmi -f soa/analyzer-service:latest; docker build -t soa/analyzer-service . ; minikube image load soa/analyzer-service:latest; kubectl apply -f deployment.yaml
# Si se quiere exponer el puerto
kubectl port-forward deployment/analyzer-service 4000:4000