"""El odulo permite comunicarse con el exchange de Rabbit para escrbir un mensaje en queue1"""
import requests

def send_message(message):
    """Enviar el mensaje al api el publisher"""
    #dentro de minikube
    api_url = "http://10.107.229.105:80/publish/queue1/" + message

    response = requests.post(api_url)
    return response.status_code
