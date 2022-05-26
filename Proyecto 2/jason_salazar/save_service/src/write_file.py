"""Este modulo permite escribir texto en un archivo"""

def write_save(file, message):
    """Agrega texto a un archivo nuevo o existente"""
    with open(file, "a", encoding="utf8") as output:
        output.write(message+'\n')

    output.close()

    return 1
