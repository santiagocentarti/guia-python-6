def leernombres(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        nombres = archivo.readlines()
    return nombres

def imprimirlista(lista):
    lista.sort()
    for nombre in lista:
        print(nombre)

archivo_nombres = "nombres.txt"

nombres = leernombres(archivo_nombres)

imprimirlista(nombres)

