
from fastapi import FastAPI
import os    

from fastapi.responses import HTMLResponse

# set the os GCP APP varibale
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'credentials.json'
TESTLINT=''

app= FastAPI()

@app.get("/",response_class=HTMLResponse)
def mainGet():
    faces=getFaces()
    feelings=feelingAnalysisFromFaces(faces)
    
    return toHtlmTable(feelings)




def toHtlmTable(feelings):


    rows=""

   ## ACA CREO LOS HEADERS
    for feelingsInfo in feelings:
        rows+=f"<tr><td>"+ str(feelingsInfo[0])+"</td><td>"+ str(feelingsInfo[1])+"</td><td>"+ str(feelingsInfo[2])+"</td><td>"+ str(feelingsInfo[3])+"</td><td>"+ str(feelingsInfo[4])+"</td></tr>"


    response="""<table style="width:100%">
                    <tr>
                        <th>Numero de Cara</th>
                        <th>Enojo</th>
                        <th>Tristeza</th>
                        <th>Felicidad</th>
                        <th>Sorpresa</th>
                    </tr>
                        """ +rows+"""

                    </table>"""

    return response

"""
DEF:
    Filtra la informacion de las caras con sus emociones en una escala del
    0 al 5, siendo 5 el valor mas alto de probabilidad de dicha emoción
PARAMS:
    faces: array de objetos de tipo FaceAnnotation
RETURNS:
    Una lista de arrays con la estructura:
    [Numero de cara, grado de enojo, grado de pena, grado de felicidad, grado de sorpresa]
"""
def feelingAnalysisFromFaces(faces):
    ## Se necesita esta escala para retornar un valor numerico
    scale = (0, 1, 2, 3,4, 5)
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


   
    
    
def main(event,context):
    
    feelings=feelingAnalysisFromFaces(faces)
    x=toHtlmTable(feelings)
    print(x)
    
#main(1,1)