#La función fue creada basándose en la función explicada de la documentación oficial de Google Cloud Platform: https://cloud.google.com/vision/docs/detecting-faces?hl=es

import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision-private-key.json'
#Instancia un cliente
client = vision.ImageAnnotatorClient()

def detect_faces(path):
	
	#Detección de rostros en una imagen
	with io.open(path, 'rb') as image_file:
		content = image_file.read()
	#Abre la imagen con el contenido de Visión
	image = vision.Image(content = content)
	#Realiza la respuesta
	response = client.face_detection(image = image)
	faces = response.face_annotations
	#Enumeración de Google Cloud
	for face in faces:
		result = {
			'Joy': face.joy_likelihood,
			'Sorrow': face.sorrow_likelihood,
			'Anger': face.anger_likelihood,
			'Surprise': face.surprise_likelihood,
		}
	return result
	

