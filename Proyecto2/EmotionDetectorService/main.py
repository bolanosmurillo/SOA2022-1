"Servicio de analisis de emociones"
import os
import pika
from google.cloud import vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'credentials.json'


def get_faces(image_content):
    """
    DEF:
        Se encarga de conseguir una imagen del bucket  y utilizar el API
        de vision
    REF:
        Codigo basado en la documentación de VISION
        https://cloud.google.com/vision/docs/detecting-faces
    """
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    # pylint: disable=no-member
    response = client.face_detection(image=image)
    result_faces = response.face_annotations
    return result_faces

def main():
    def callback(ch, method, properties, body):
        print(get_faces(body))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detectEmotion')
    channel.basic_consume(queue='detectEmotion', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()

main()
