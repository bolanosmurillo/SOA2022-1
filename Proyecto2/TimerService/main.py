"""Servicio de obtencion de fecha """
import datetime
import pytz
import pika

def get_time():
    """
    DEF:
        Se encarga de activar el proceso de obtencion de las imagenes una vez la hora se cumpla

    """
    get_images = False
    hour=0
    while True:
        fecha = datetime.datetime.now(tz=pytz.timezone('America/Costa_Rica'))
        print("target:"+ str(hour))
        print("current:"+ str(fecha.hour))
        if fecha.hour == hour and not get_images:
            get_images = True
            send_signal()
            break
        if fecha.hour != hour:
            get_images = False

def send_signal():
    """
    Envia la senal de tiempo
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='timeSignal')
    channel.basic_publish(exchange='',
                      routing_key='timeSignal',
                      body="Time!")
    print(" TIMER_SERVICE: Mensaje Enviado")
    connection.close()

get_time()
