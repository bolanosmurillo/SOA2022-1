import boto3
import os

from google.cloud import vision_v1
from google.cloud.vision_v1 import types



def printEmotions(name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'soaproyect1-1270e3463763.json'
    
    #instance a client
    client = vision_v1.ImageAnnotatorClient()

    #set the image
    image = types.Image()
    image.source.image_uri = 'https://storage.googleapis.com/soa_bucket_project/persona1.jpg'

    #face detection
    response_face = client.face_detection(image=image)
    face_data = []

    for face_detection in response_face.face_annotations:
        d = {
            'confidence': face_detection.detection_confidence
        }
        print(d)
        return d




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printEmotions('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
