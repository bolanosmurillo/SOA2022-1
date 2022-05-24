"Servicio encargado de obtener las imagenes del bucket"
import os
import pika
from google.cloud import storage

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
    Envia la imagen como mensaje al detector de emociones
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detectEmotion')
    channel.basic_publish(exchange='',
                      routing_key='detectEmotion',
                      body=get_image())
    print(" READER_SERVICE: Mensaje Enviado")
    connection.close()

def main():
    def callback(ch, method, properties, body):
        print(send_messagge())

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='timeSignal')
    channel.basic_consume(queue='timeSignal', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()

main()
