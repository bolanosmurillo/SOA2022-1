"""Writer Service"""

def write():
    """
    DEF:
        Escribe el documento de resultados
    """
    resultados = [["Face Index", "Enojo", "Tristeza", "Felicidad", "Sorpresa"],
                ["Face Index", "Enojo", "Tristeza", "Felicidad", "Sorpresa"],
                ["Face Index", "Enojo", "Tristeza", "Felicidad", "Sorpresa"] ]
    file= open("aha/example.txt","a+", encoding="utf-8")
    for fila in resultados:
        linea = ""
        for columna in fila:
            linea = linea + " " + str(columna)
        file.write(linea)
        file.write("\n")
    file.close()
write()