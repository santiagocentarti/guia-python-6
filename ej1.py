nombre = input ("Ingrese un nombre: ")
apellido = input ("Ingrese un apellido: ")

nombrecompleto = "\n"+nombre+" "+apellido

with open("nombres.txt","a",encoding="utf-8") as archivo:
    archivo.write(nombrecompleto)