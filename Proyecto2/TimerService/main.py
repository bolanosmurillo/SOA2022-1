"""Servicio de obtencion de fecha """
import datetime
import pytz
import pika


def get_time():
    """
    DEF:
        Se encarga de activar el proceso de obtencion de las imagenes una vez la hora se cumpla

    """
    hour=10
    mesagge_sent=False
    while True:
        fecha = datetime.datetime.now(tz=pytz.timezone('America/Costa_Rica'))
        print("target:"+ str(hour))
        print("current:"+ str(fecha.hour))
        if fecha.hour == hour and not mesagge_sent:
            mesagge_sent = True
            send_signal()
            break
        if fecha.hour != hour:
            mesagge_sent = False

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
