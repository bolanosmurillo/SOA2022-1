import os    

from google.cloud import vision 
from google.cloud.vision_v1 import types
from google.cloud import storage
from tabulate import tabulate

# set the os GCP APP varibale
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'credentials.json'
TESTLINT=''

"""
DEF:
    Esta funcion se encarga de tomar una foto almacenada en el bucket
RETURNS:
    La imagen como bytes
"""
def getImage():
    client = storage.Client()
    
    bucket = client.get_bucket('proyectosoa2022')
    
    blob = bucket.get_blob('person.jpg')
    return blob.download_as_bytes()  

"""
DEF: 
    Se encarga de conseguir una imagen del bucket  y utilizar el API
    de vision
    
REF: 
    Codigo basado en la documentación de VISION
    https://cloud.google.com/vision/docs/detecting-faces
"""
def getFaces():
    client = vision.ImageAnnotatorClient()

    imageContent=getImage()
    image = vision.Image(content=imageContent)

    response = client.face_detection(image=image)
    faces = response.face_annotations
    return faces

    

"""
DEF:
    Filtra la informacion de las caras con sus emociones en una escala del
    0 al 5, siendo 5 el valor mas alto de probabilidad de dicha emoción
PARAMS:
    faces: array de objetos de tipo FaceAnnotation
RETURNS:
    Una lista de arrays con la estructura:
    [Numero de cara, grado de enojo, grado de pena, grado de felicidad, grado de sorpresa]
"""
def feelingAnalysisFromFaces(faces):
    ## Se necesita esta escala para retornar un valor numerico
    scale = (0, 1, 2, 3,4, 5)
    response=[]
    for faceIndex in range(0,len(faces)):
        face=faces[faceIndex]
        faceInfo=["Cara {}".format(faceIndex)]
        faceInfo.append(scale[face.anger_likelihood])
        faceInfo.append(scale[face.sorrow_likelihood])
        faceInfo.append(scale[face.joy_likelihood])
        faceInfo.append(scale[face.surprise_likelihood])
        response.append(faceInfo)
    return response


"""
DEF: 
    Se encarga de imprimir en una tabla bonita el resultado de los feelings
PARAMS:
    Array de arrays de sentimientos con la siguiente estructura
    [["Face Index", "Enojo", "Tristeza", "Felicidad", "Sorpresa"]]
"""
def prettyPrint(feelings):

    table=[]
    headers= ["Numero de Cara", "Enojo", "Tristeza", "Felicidad", "Sorpresa"]

   ## ACA CREO LOS HEADERS
    for feelingsInfo in feelings:
        table.append(feelingsInfo)
    
    print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
    
    
def main(event,context):
    faces=getFaces()
    feelings=feelingAnalysisFromFaces(faces)
    prettyPrint(feelings)
    

main()
