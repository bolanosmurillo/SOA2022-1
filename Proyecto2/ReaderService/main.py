"Servicio encargado de obtener las imagenes del bucket"
import os
import pika
from google.cloud import storage

# set the os GCP APP varibale
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'credentials.json'

BUCKET_NAME="soabucket314"
IMAGE_CUANTITY_LIMIT=10

def get_image(filename):

    """
    DEF:
        Esta funcion se encarga de tomar una foto almacenada en el bucket
    RETURNS:
        La imagen como bytes
    """
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.get_blob(filename)
    ##diez imagenes
    return blob.download_as_bytes()
def get_all_files_in_bucket():
    """
    DEF:
        Consigue todos los nombres de los archivos en el bucket,
        posteriormente obtiene los archivos  y los retorna
    """
    client = storage.Client()
    blobs = client.list_blobs(BUCKET_NAME)
    result=[]
    
    for index,blob in enumerate( blobs):
        if index >=IMAGE_CUANTITY_LIMIT: break
        file=get_image(blob.name)
        result.append(file)
    return result

def send_messagge(mesagge):

    """
    Envia la imagen como mensaje al detector de emociones
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detectEmotion')
    channel.basic_publish(exchange='',
                      routing_key='detectEmotion',
                      body=mesagge)
    print(" READER_SERVICE: Mensaje Enviado")
    connection.close()

def send_all_files():
    """
    DEF:
        Recopilado de las operaciones anteriores, envia todas las
        imagenes al servicio de deteccion de emociones
    """
    files=get_all_files_in_bucket()
    for  file in files:
        send_messagge(file)


def main():
    def callback(ch, method, properties, body):
        send_all_files()

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='timeSignal')
    channel.basic_consume(queue='timeSignal', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()

main()

