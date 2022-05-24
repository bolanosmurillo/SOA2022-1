"""Writer Service"""
import pika
from tabulate import tabulate
IMAGE_CUANTITY_LIMIT=10
feelings_analysis=[]

def pretty_print(feelings):
    """
    DEF: 
        Se encarga de imprimir en una tabla bonita el resultado de los feelings
    PARAMS:
        Array de arrays de sentimientos con la siguiente estructura
        [["Face Index", "Enojo", "Tristeza", "Felicidad", "Sorpresa"]]
    """
    table=[]
    headers= ["Numero de Cara", "Enojo", "Tristeza", "Felicidad", "Sorpresa"]

   ## ACA CREO LOS HEADERS
    for feelings_Info in feelings:
        table.append(feelings_Info)
    
    return tabulate(table, headers=headers, tablefmt='fancy_grid')

def write(emotions):
    """
    DEF:
        Escribe el documento de resultados
    """
    result =str(emotions)
    result=result[1::].replace('"',"").replace("[","").replace("]","")
    feelings_analysis.append(result.split(','))
    if len(feelings_analysis)< IMAGE_CUANTITY_LIMIT:
        return
    
    table=pretty_print(feelings_analysis)
    file= open("aha/example.txt","a+", encoding="utf-8")
    file.write(table)

    print("[*] Archivo escrito con exito")
    file.close()

def enable_listenning():
    """
    DEF:
        Activa la escucha de mensajes 
    """
    def callback(ch, method, properties, body):
        write(body)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='writeSignal')
    channel.basic_consume(queue='writeSignal', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()

enable_listenning()
