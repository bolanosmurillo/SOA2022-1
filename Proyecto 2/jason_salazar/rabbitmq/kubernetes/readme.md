# Crear un namaspace para Rabbit
    kubectl create ns rabbits

# Deploymet
    kubectl apply -n rabbits -f .\kubernetes\rabbit-rbac.yaml
    kubectl apply -n rabbits -f .\kubernetes\rabbit-secret.yaml
    kubectl apply -n rabbits -f .\kubernetes\rabbit-configmap.yaml
    kubectl apply -n rabbits -f .\kubernetes\rabbit-statefulset.yaml

# Para acceder Rabbit por medio de UI
    kubectl -n rabbits port-forward rabbitmq-0 8080:15672

    Ir a htttp://localhost:8080 
    Usar Username: guest 
         Password: guest


# Automatic Synchronization
Esto es estra, para sincronizar todos los nodos de Rabbit
https://www.rabbitmq.com/ha.html#unsynchronised-mirrors

1. kubectl -n rabbits get pods
2. kubectl -n rabbits exec -it rabbitmq-0 -- bash
3. Pegar el comando(Sin las comillas):
```
rabbitmqctl set_policy ha-fed \
    ".*" '{"federation-upstream-set":"all", "ha-sync-mode":"automatic", "ha-mode":"nodes", "ha-params":["rabbit@rabbitmq-0.rabbitmq.rabbits.svc.cluster.local","rabbit@rabbitmq-1.rabbitmq.rabbits.svc.cluster.local","rabbit@rabbitmq-2.rabbitmq.rabbits.svc.cluster.local"]}' \
    --priority 1 \
    --apply-to queues
```