#define main(event, context):
#	print("Evento-contexto", context)


import io
from google.cloud import vision
#Instancia un cliente
client = vision.ImageAnnotatorClient()

def detect_faces(bucket, filename):
	#Detección de rostros en una imagen
	with io.open(path, 'rb') as image_file:
		content = image_file.read()
	#Abre la imagen con el contenido de Visión
	image = vision.Image(source = vision.ImageSource(gcs_image_uri=f"gs://{bucket}/{filename}"))
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

def main(file, context):
	#Obtiene la información del bucket
	bucket = validate_message(file, "bucket")
	name = validate_message(file, "name")
	#Llamada a la función
	detect_faces(bucket, name)
	print("File {} processed.".format(file["name"]))


	
