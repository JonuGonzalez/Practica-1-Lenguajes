import json

def cargar(archivo):
    with open(archivo+'.json') as file:
        data = json.load(file)
        print("Archivo Cargado Correctamente")
    file.close()
    array = data
    print(array)
    return array

