"""El modulo permite comunicarse con el exchange de Rabbit para escrbir mensaje en queue2"""
import requests

def send_message(message):
    """Enviar el mensaje al api el publisher"""
    #dentro de minikube
    api_url = "http://10.107.229.105:80/publish/queue2/" + message

    response = requests.post(api_url)
    return response.status_code
