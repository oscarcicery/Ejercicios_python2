#_______________________________________PROGRAMANDO POR ABURRIMEINTO PARTE CUATRO
'''Hacer programa que realice:
 gestione y administre los parqueaderos de una empresa.


Requerimientos:
Capacidad maxima 200 cupos.

3 bicicletas son un cupo.
1 carro es un cupo
2 motos son un cupo

-------

Costo parqueadero:
Hora por carro: 5000 pesos
hora por moto: 2500 pesos
hora por bicicletas 1000 pesos

--------

Beneficios:
Cliente: 20% descuento
adulto mayor: 10%
discapacitado: 15%



------------
MOSTRAR
El valor a pagar cuando se saque un vehiculo
el cupo actual



Estos descuetos solo son acumulaables si es un cliente.

'''


#______________________________LISTAS
vehiculos=[]
usuarios={}
entrada=[]
salida=[]

#_______________________________Variables
cupomax=200.0
run=1
cupo2=0.0
des=0.0

#_______________________________Funcion para ingresar vehiculos
def ingreso(tipovehiculo):
    cupo=0
    vehiculos.append(tipovehiculo)
    if(tipovehiculo==1):
        cupo=1
    elif(tipovehiculo==2):
        cupo=0.5
    else:
        cupo=1/3
    return cupo


#_________________________________Mostrar vehiculos
def mostrarvehiculos():
    i=0
    for i in range(len(vehiculos)):
        print("Vehiculo #",i+1," es ",vehiculos[i],"\n")

#________________________________Funcion para calcular el valor a pagar por vehiculo
def descuento(tipouser):
    descuento=0
    if(tipouser==1):
        descuento=0.2
    elif(tipouser==2):
        desceunto=0.10
    elif(tipouser==3):
        descuento=0.15
    return descuento

#__________________________________Funcion para calcular el costo por hora de parqueo de cada vehiculo
def costovehiculo(tipovehiculo):
    costo=0
    if(tipovehiculo==1):
        costo=5000
    elif(tipovehiculo==2):
        costo=2500
    elif(tipovehiculo==3):
        costo=1000
    return costo

#__________________________________Funcion para salida de vehiculos
def tiempo():
    return 0

#___________________________________INICIO PROGRAMA
while run==1:
    a=int(input("DIGITE 1 PARA INGRESAR VEHICULO, 2 PARA SACAR, 3 PARA VER CUPO DISPONIBLE O OTRO PARA SALIR\n"))
    if (a==1):
        tipouser=int(input("ingrese el tipo de usuario: 1=cliente; 2=adulto; 3=discapacitado\n"))
        des=descuento(tipouser)
        tipovehiculo=int(input("ingrese el tipo de vehiculo: 1=carro; 2=moto; 3=bici\n"))
        cupo2=cupo2+ingreso(tipovehiculo)




    elif(a==2):
        run=0
    elif(a==3):
        run=0
print("el cupo disponible es ",cupomax-cupo2,"\n")
mostrarvehiculos()
