#CODIGO ORIGINAL
# EJERCICIO

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


# inicio Ciclo
cantidad_de_produ=int(input())
for i in range (cantidad_de_produ):
        codigo_de_produc = int( input())
        nombre_de_produc =(input())
        cantidad_producto_compra = int(input())
        valor_unitar = float(input())
        tipo_iv = int(input())


    # agrega valores a las listas
        codigo_de_producto.append(codigo_de_produc)
        nombre_producto.append(nombre_de_produc)
        cantidad_de_prod.append(cantidad_producto_compra)
        valor_unit.append(valor_unitar)

    #condicionales para tipo de iva
        if(tipo_iv==1):
            iva=0.0
            lista_valor_final.append(cantidad_producto_compra*valor_unitar)
            total=total+cantidad_producto_compra*valor_unitar
            total_iva=total_iva+(cantidad_producto_compra*valor_unitar*0)
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
       
   
print(len(codigo_de_producto))
print(len(nombre_producto))
print(len(cantidad_de_prod))
print(len(valor_unit))
print(len(lista_tipo_iva))

for j in range(len(lista_tipo_iva)):
    print(codigo_de_producto[j])
    print(nombre_producto[j])
    print(lista_valor_producto[j])
    print(lista_valor_final[j])
   
print(total)
print(total_iva)