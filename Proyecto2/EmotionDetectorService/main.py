"Servicio de analisis de emociones"
from email import message
import os
import pika
from google.cloud import vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'C:/Users/adrii/OneDrive/Escritorio/SOA2022-1/Proyecto2/EmotionDetectorService/credentials.json'
client = vision.ImageAnnotatorClient()

def get_faces(image_content):
    """
    DEF:
        Se encarga de conseguir una imagen del bucket  y utilizar el API
        de vision
    REF:
        Codigo basado en la documentación de VISION
        https://cloud.google.com/vision/docs/detecting-faces
    """
    
    image = vision.Image(content=image_content)
    # pylint: disable=no-member
    response = client.face_detection(image=image)
    result_faces = response.face_annotations
    return result_faces



def feeling_analysis_from_faces(faces):
    """
    DEF:
        Filtra la informacion de las caras con sus emociones en una escala del
        0 al 5, siendo 5 el valor mas alto de probabilidad de dicha emoción
    PARAMS:
        faces: array de objetos de tipo FaceAnnotation
    RETURNS:
        Una lista de arrays con la estructura:
        [Numero de cara, grado de enojo, grado de pena, grado de felicidad, grado de sorpresa]
    """
    ## Se necesita esta escala para retornar un valor numerico
    scale = (0, 1, 2, 3,4, 5)
    response=[]
    for face_index , face in enumerate(faces):
        face_info=["Cara" +str(face_index)]
        face_info.append(scale[face.anger_likelihood])
        face_info.append(scale[face.sorrow_likelihood])
        face_info.append(scale[face.joy_likelihood])
        face_info.append(scale[face.surprise_likelihood])
        response.append(face_info)
    return response

def send_messagge(mesagge):
    """
    Envia la imagen como mensaje al escritor
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='writeSignal')
    channel.basic_publish(exchange='',
                      routing_key='writeSignal',
                      body=str(mesagge))
    print(" READER_SERVICE: Mensaje Enviado")
    connection.close()

def enable_listenning():
    """
    DEF:
        Activa la escucha de mensajes 
    """
    def callback(ch, method, properties, body):
        faces=get_faces(body)
        analisys=feeling_analysis_from_faces(faces)
        send_messagge(analisys)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='detectEmotion')
    channel.basic_consume(queue='detectEmotion', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()

enable_listenning()
