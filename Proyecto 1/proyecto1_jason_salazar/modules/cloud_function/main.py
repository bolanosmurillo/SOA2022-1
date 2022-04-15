import emotion_detection

def main(event , context):

    uri_base = event['bucket'] #Bucket donde esta la imagen
    pic = event['name']        #Nombre de la imagen a analizar

    result = emotion_detection.emo_detect(uri_base, pic) #Detectar emocion
    
    print("Emocion detectada: "+result[0]+", Probabilidad: "+result[1])
