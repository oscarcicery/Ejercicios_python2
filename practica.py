'''HACER UN PROGRAMA QUE:

Me pida un mensaje y si el mensaje tiene más vocales que consonantes mostrar 1, en otro caso mostrar 0

'''

mensaje=""

def cadena(mensaje):
    contador=0
    for letra in mensaje:
        if letra.lower() in "aeiou":
            contador+=1
    return contador

def consonantes(mensaje):
    contador=len(mensaje)
    for i in mensaje:
        if i.lower() in "aeiou":
            contador=contador-1
    return contador
mensaje=input("Ingrese el mensaje")
numvocales=cadena(mensaje)
numconsonantes=consonantes(mensaje)
def calcular(numvocales, numconsonantes):
    resultado=0
    if (numconsonantes<numvocales):
        resultado=1
    return print(resultado)

solucion=calcular(numvocales, numconsonantes)
