"""Este modulo detecta la emocion en la imagen"""
import time
import emotion_detection
import queue_connection

def start_analyzer():
    """Permite detectar las emociones las imagenes"""
    response_ = 0

    uri_base = 'image_source_soa'

    date = "Fecha y hora " + time.strftime("%c")
    queue_connection.send_message(date)

    for image_number in range(1,11):
        pic = str(image_number)+'.jpg'

        result = emotion_detection.emo_detect(uri_base, pic) #Detectar emocion

        message = "Foto "+str(image_number)
        message = message+": Emocion detectada: "+result[0]+" Probabilidad: "+result[1]

        response_ = queue_connection.send_message(message)

    return response_
