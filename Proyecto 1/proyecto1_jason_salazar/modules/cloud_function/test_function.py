"""Este modulo detecta la emocion en la imagen"""
import emotion_detection

def test_emo_detect():
    """Prueba unitaria de la funcion emo_detect"""

    #public data
    test_uri_base = 'cloud-vision-codelab'
    test_pic = 'face_surprise.jpg'

    result = emotion_detection.emo_detect(test_uri_base, test_pic)


    assert result[0] == "Surprice"
    assert result[1] == "LIKELY"
