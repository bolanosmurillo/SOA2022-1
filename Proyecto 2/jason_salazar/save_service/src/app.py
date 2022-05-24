"""Este modulo permite guardar los resultados del analisis en un archivo compartido"""
import os
import pika
import write_file
rabbit_host = os.getenv("RABBIT_HOST")
rabbit_port = os.getenv("RABBIT_PORT")
rabbit_user = os.getenv("RABBIT_USERNAME")
rabbit_password = os.getenv("RABBIT_PASSWORD")

def on_message_received(cha, method, properties, body):
    """Permite mandar a escribir el mensaje en un archivo de salida"""
    message = f"{body.decode()}"

    result = write_file.write_save("../host/output.txt", message)

    if result == 1:
        #Indicar a la cola que el mesaje ya fue procesado
        cha.basic_ack(delivery_tag = method.delivery_tag)

#Se establecen los parametros para la conexion
credentials = pika.PlainCredentials(rabbit_user, rabbit_password)
parameters = pika.ConnectionParameters(rabbit_host, rabbit_port,'/',credentials)

#Se establecen conexion
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Se establece la cola y se empieza a consumir
channel.queue_declare(queue='queue2',durable=True)
channel.basic_consume(queue='queue2', auto_ack=False, on_message_callback=on_message_received)
channel.start_consuming()
