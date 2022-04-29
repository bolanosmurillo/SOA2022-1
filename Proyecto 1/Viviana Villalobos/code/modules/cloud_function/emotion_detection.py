"""
Emotion detection. Will call caloud API to get the best emotion
"""
from google.cloud import vision_v1
import os

def get_best(emotion_str, likely, emotion_try):
    """
    Returns the best emotion or most likely found
    """
    likely = likely.replace('Likelihood.', '')
    if likely == "VERY_LIKELY":
        return (emotion_str,likely)
    if (likely == "LIKELY" and emotion_try[1] != "VERY_LIKELY" ):
        return (emotion_str,likely)
    if  (likely == "POSSIBLE" and emotion_try[1] == "-" ):
        return (emotion_str,likely)

    return emotion_try

def get_emotion(pic_name):
    """
    calls the API to get the emotions
    """
    client = vision_v1.ImageAnnotatorClient()
    image = vision_v1.Image()
    image.source.image_uri = "https://storage.googleapis.com/soa_bucket_project/" + pic_name

    response_face = client.face_detection(image=image)
    face = response_face.face_annotations[0]

    emotion = ("None","-")
    emotion =  get_best("Anger", str(face.anger_likelihood), emotion)
    emotion =  get_best("Joy", str(face.joy_likelihood), emotion)
    emotion =  get_best("Surprice", str(face.surprise_likelihood),emotion)
    emotion =  get_best("Sorrow", str(face.sorrow_likelihood),emotion)

    return emotion
