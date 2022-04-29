import os    

from google.cloud import vision 
from google.cloud.vision_v1 import types
from google.cloud import storage
from tabulate import tabulate

# set the os GCP APP varibale
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'soa2022-1-a4e8e7e2fd24.json'
TESTLINT=''

def get_image_bytes_from_bucket():
    client = storage.Client()
    bucket = client.get_bucket('soa2022-1')
    blob = bucket.get_blob('person.jpg')
    return blob.download_as_bytes()  

"""
    Codigo basado en la documentación de VISION
    https://cloud.google.com/vision/docs/detecting-faces
"""
def get_faces():
    client = vision.ImageAnnotatorClient()
    imageContent=get_image_bytes_from_bucket()
    image = vision.Image(content=imageContent)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    return faces 

def analize_face_feelings(faces):
    scale = (0, 1, 2, 3, 4, 5)
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
PARAMS:
    Array de arrays de sentimientos con la siguiente estructura
    [["Face Index", "Enojo", "Tristeza", "Felicidad", "Sorpresa"]]
"""
def print_table(feelings):
    table=[]
    headers= ["Numero de Cara", "Enojo", "Tristeza", "Felicidad", "Sorpresa"]
    for feelingsInfo in feelings:
        table.append(feelingsInfo)
    
    print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
    
    
def main():
    faces=get_faces()
    feelings=analize_face_feelings(faces)
    print_table(feelings)

main()