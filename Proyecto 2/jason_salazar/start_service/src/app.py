"""Este modulo permite al usuario activar el proceso de analisis de las imagenes"""
import time
from flask import Flask, jsonify
import queue_connection

app = Flask(__name__)


@app.route('/start_analyze')
def init_handler():
    """Permite indicar que se debe iniciar el proceso de analisis"""
    response_ = queue_connection.send_message("start_analyze")
    date =  time.strftime("%c")
    return jsonify({"Proceso":"Iniciado", "Status Code":response_, "Fecha":date})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4001, debug=True)
