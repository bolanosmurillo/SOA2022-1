"""Este modulo detecta la emocion en la imagen"""
import emotion_detection

def test_emo_detect():

    result = emotion_detection.emo_detect("persona1.jpg")


    assert result[0] == "Joy"
    assert result[1] == "VERY_LIKELY"
