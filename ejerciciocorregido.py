# EJERCICIO

# PARA CADA PRODUCTO N MOSTRAR:

#codigo
#nombre
#valor sin iva
#valor con iva


#Valor final de la compra
#valor final del iva

#SE DEBE IMPRIMIR DE MANERA ASCENDENTE SEGÚN EL CODIGO DEL PRODUCTO

# definición variables
codigo_de_produc =0
nombre_de_produc =""
cantidad_producto_compra =0
valor_unitar =0.0
tipo_iv =0
total=0.0
total_iva=0.0

# definición listas:
codigo_de_producto=[]
nombre_producto=[]
cantidad_de_prod=[]
valor_unit=[]
lista_tipo_iva=[]
lista_valor_producto=[]
lista_valor_iva=[]
lista_valor_final=[]

#definicion diccionarios
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}



# inicio Ciclo
cantidad_de_produ=int(input())

for i in range (cantidad_de_produ):
        codigo_de_produc = int( input())
        nombre_de_produc =articulos.get(codigo_de_produc, "no existe dato para esta clave")
        cantidad_producto_compra = int(input())
        valor_unitar=int(precios.get(codigo_de_produc, "no existe dato para esta clave"))
        tipo_iv = int(input())


    # agrega valores a las listas
        codigo_de_producto.append(codigo_de_produc)
        nombre_producto.append(nombre_de_produc)
        cantidad_de_prod.append(cantidad_producto_compra)
        valor_unit.append(valor_unitar)

    #condicionales para tipo de iva
        if(tipo_iv==1):
            iva=0.0
            total=total+cantidad_producto_compra*valor_unitar
            total_iva=total_iva+(cantidad_producto_compra*valor_unitar*0)
            lista_valor_final.append(cantidad_producto_compra*valor_unitar)

        elif(tipo_iv== 2):
            iva= 0.05
            total=total+cantidad_producto_compra*valor_unitar*1.05
            total_iva=total_iva+(cantidad_producto_compra*valor_unitar*0.05)
            lista_valor_final.append(cantidad_producto_compra*valor_unitar*1.05)

        else:
            iva =  0.19
            total=total+cantidad_producto_compra*valor_unitar*1.19
            total_iva=total_iva+(cantidad_producto_compra*valor_unitar*0.19)
            lista_valor_final.append(cantidad_producto_compra*valor_unitar*1.19)

        lista_tipo_iva.append(tipo_iv)
        lista_valor_producto.append(cantidad_producto_compra*valor_unitar)
        lista_valor_iva.append(cantidad_producto_compra*valor_unitar*iva)
       
   
j=0
for j in range(len(codigo_de_producto)):
    print(codigo_de_producto[j])
    print(nombre_producto[j])
    print(lista_valor_producto[j])
    print(lista_valor_final[j])
   
print(total)
print(total_iva)


