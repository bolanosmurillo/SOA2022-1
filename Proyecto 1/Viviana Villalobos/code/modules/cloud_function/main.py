"""
Main funct that called the emotion detection one
"""
import emotion_detection

def main(event):
    """
    Main that calls with the image
    """
    image = event['name']

    result = emotion_detection.get_emotion(image)

    print("Emotion: "+result[0]+" : "+result[1])
