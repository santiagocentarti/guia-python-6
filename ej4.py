def generadorNombre():

    import random

    nombres = ["Ramiro","Fermin","Santiago","Nicolas","Guillermo","Mateo","Facundo","Joaquin","Salvador","Matias"]
    apellidos = ["Bravo","Martinez","Gonzales","chavarria","Salomon","Garcia","Villanueva","Mantilla","Prados","Santini","centarti"]
    lista = []

    for i in range(10):
        
        nombrecompleto = random.choice(nombres)+" "+random.choice(apellidos)

        lista.append(nombrecompleto)

    lista.sort()

    return lista

lista = generadorNombre()

listaNombre =" "

for elemento in lista:
    listaNombre += "\n"+elemento

print(listaNombre)

with open("nombres.txt","a",encoding="utf-8") as archivo:
    archivo.write(listaNombre)