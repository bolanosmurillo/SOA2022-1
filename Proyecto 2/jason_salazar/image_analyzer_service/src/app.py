"""El modulo permite leer a queue1 y ejecutar el procesos de analisis de la imagenes"""
import os
import pika
import analyzer
rabbit_host = os.getenv("RABBIT_HOST")
rabbit_port = os.getenv("RABBIT_PORT")
rabbit_user = os.getenv("RABBIT_USERNAME")
rabbit_password = os.getenv("RABBIT_PASSWORD")


def on_message_received(cha, method, properties, body):
    """Este activa el proceso de analizar las imagenes"""
    result = analyzer.start_analyzer()
    if result == 200:
        #Se indica a la cola queue1 que el mesaje ya fue procesado
        cha.basic_ack(delivery_tag = method.delivery_tag)

#Se establecen los parametros para la conexion
credentials = pika.PlainCredentials(rabbit_user, rabbit_password)
parameters = pika.ConnectionParameters(rabbit_host, rabbit_port,'/',credentials)

#Se establecen conexion
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Se establece la cola y se empieza a consumir
channel.queue_declare(queue='queue1',durable=True)
channel.basic_consume(queue='queue1', auto_ack=False, on_message_callback=on_message_received)
channel.start_consuming()
