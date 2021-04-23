from iteration_utilities import deepflatten


## Imprimir el vector aplanado
def printList(vector):

    if type(vector) != list:
        return "No envio un arreglo valido"

    if not vector:
        return "El Arrelgo que mando está Vacio"

    if validateListInt(vector):
        return "ERROR: Los datos enviados contienen valores no validos"

    planeList = list(deepflatten(vector))

    return planeList


def validateListInt(vector):

    for element in vector:
        if isinstance(element, list):
            validateListInt(element)
        else:
            if type(element) != int:
                return True

    return False
