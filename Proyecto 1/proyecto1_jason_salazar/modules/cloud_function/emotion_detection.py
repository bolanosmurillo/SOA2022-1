##from __future__ import print_function
"""Modulo necesario para utiliza Google Vsion API"""
from google.cloud import vision

def get_most_likely(emo, likelihood, most_likely_emotion):
    """Dado dos emociones conserva la de mayor probabilidad"""
    likelihood = likelihood.replace('Likelihood.', '')
    if( likelihood == "VERY_LIKELY"):
        return (emo,likelihood)
    elif (likelihood == "LIKELY" and most_likely_emotion[1] != "VERY_LIKELY" ):
        return (emo,likelihood)
    elif  (likelihood == "POSSIBLE" and most_likely_emotion[1] == "-" ):
        return (emo,likelihood)
    else:
        return most_likely_emotion

def get_emotion(face):
    """Permite seleccionar la emocion mas probable"""
    most_likely_emotion = ("Ninguna","-")
    most_likely_emotion =  get_most_likely("Anger", str(face.anger_likelihood), most_likely_emotion)
    most_likely_emotion =  get_most_likely("Joy", str(face.joy_likelihood), most_likely_emotion)
    most_likely_emotion =  get_most_likely("Surprice", str(face.surprise_likelihood), most_likely_emotion)

    return most_likely_emotion

def emo_detect(uri_base, pic):
    """Permite detectar la emocion de un rosto en una imagen"""
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = 'gs://%s/%s' % (uri_base, pic)

    response = client.face_detection(image=image)# pylint: disable=no-member
    face = response.face_annotations[0]

    return get_emotion(face)
