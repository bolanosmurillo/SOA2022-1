"Servicio encargado de obtener las imagenes del bucket"
import os
from google.cloud import storage
import pika
# set the os GCP APP varibale
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'credentials.json'


def get_image():
    """
    DEF:
        Esta funcion se encarga de tomar una foto almacenada en el bucket
    RETURNS:
        La imagen como bytes
    """
    client = storage.Client()
    bucket = client.get_bucket('soabucket314')
    blob = bucket.get_blob('person.jpg')
    ##diez imagenes
    return blob.download_as_bytes()


def send_messagge():
    """
    Envia el mensaje al detector de emociones
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detectEmotion')
    channel.basic_publish(exchange='',
                      routing_key='detectEmotion',
                      body=get_image())
    print(" READER_SERVICE: Mensaje Enviado")
    connection.close()

send_messagge()