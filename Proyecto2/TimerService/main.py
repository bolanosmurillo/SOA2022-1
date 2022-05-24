"""Servicio de obtencion de fecha """
import datetime
import pytz

def get_time():
    """
    DEF:
        Se encarga de activar el proceso de obtencion de las imagenes una vez la hora se cumpla

    """
    get_images = False
    hour=17
    while True:
        fecha = datetime.datetime.now(tz=pytz.timezone('America/Costa_Rica'))
        print("target:"+ str(hour))
        print("current:"+ str(fecha.hour))
        if fecha.hour == hour and not get_images:
            get_images = True
            break
        if fecha.hour != hour:
            get_images = False

get_time()
