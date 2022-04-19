"""
Unit test
"""
import emotion_detection

def test_get_emotion():

    result = emotion_detection.get_emotion('persona1.jpg')


    assert result[0] == "Joy"
    assert result[1] == "VERY_LIKELY"
