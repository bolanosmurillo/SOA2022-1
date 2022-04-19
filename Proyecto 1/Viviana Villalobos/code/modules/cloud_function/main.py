"""
Main funct that called the emotion detection one
"""
import emotion_detection

def main(event):
    """
    Main that calls with the image
    """
    image = event['name']        #Nombre de la imagen a analizar

    result = emotion_detection.get_emotion(image) #Detectar emocion

    print("Emotion: "+result[0]+" : "+result[1])
