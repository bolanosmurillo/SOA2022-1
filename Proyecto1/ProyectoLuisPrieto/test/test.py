#Código extraído de la documentación oficial de Google Cloud Platform: https://cloud.google.com/vision/docs/detecting-faces?hl=es

import os
import io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'proyecto1-luis-4b691533b4bd.json'

def detect_faces(path):
	#Instancia un cliente
	client = vision.ImageAnnotatorClient()
	#Detección de rostros en una imagen
	with io.open(path, 'rb') as image_file:
		content = image_file.read()
	#Abre la imagen con el contenido de Visión
	image = vision.Image(content = content)
	#Realiza la respuesta
	response = client.face_detection(image = image)
	faces = response.face_annotations
	#Enumeración de Google Cloud
	print('Faces:')
	for face in faces:
		result = {
			'Joy': face.joy_likelihood,
			'Sorrow': face.sorrow_likelihood,
			'Anger': face.anger_likelihood,
			'Surprise': face.surprise_likelihood,
		}
		print(result)

detect_faces("images.jpeg")