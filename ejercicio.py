



def ordenamiento_burbuja(codigo_de_produc,cantidad_producto_compra,valor_unitario,iva,nombre_de_produc,valor_producto,valor_final):
    t_nombre=""
    t_codigo=0
    t_cantidad=0
    t_valor_unitario=0.0
    t_iva=0.0
    t_valor=0.0
    t_valor_final=0.0
    N=len(codigo_de_produc)
    for i in range(0,N-1):
        for j in range(i+1,N):
            if nombre_de_produc[i]>nombre_de_produc[j]:
                t_codigo=codigo_de_produc[i]
                codigo_de_produc[i]=codigo_de_produc[j]
                codigo_de_produc[j]=t_codigo

                t_nombre=nombre_de_produc[i]
                nombre_de_produc[i]=nombre_de_produc[j]
                nombre_de_produc[j]=t_nombre

                t_cantidad=cantidad_producto_compra[i]
                t=cantidad_producto_compra[i]=cantidad_producto_compra[j]
                cantidad_producto_compra[j]=t_cantidad

                t_valor_unitario=valor_unitario[i]
                valor_unitario[i]=valor_unitario[j]
                valor_unitario[j]=t_valor_unitario

                t_iva=iva[i]
                iva[i]=iva[j]
                iva[j]=t_iva

                t_valor=valor_producto[i]
                valor_producto[i]=valor_producto[j]
                valor_producto[j]=t_valor

                t_valor_final=valor_final[i]
                valor_final[i]=valor_final[j]
                valor_final[j]=t_valor_final
    return
    codigo,nombre,cantidad,valor_unitario,iva,valor_producto,valor_final  
N=int(input(" ingrese productos"))

articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}

#Donde la clave es el código del artículo y el valor es el nombre del producto

precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

total_ventas=0
total_iva=0

# definición listas:

codigo_de_produc =[]
nombre_de_produc =[]
cantidad_producto_compra=[]
valor_unitario =[]
valor_iva=[]
tipo_iv =[]
valor_producto=[]
iva=[]
valor_final=[]

# inicio Ciclo
# agrega valores a las listas

for i in range (N):
    codigo_de_produc.append(int(input()))
    cantidad_producto_compra.append(float(input()))
    tipo_iv.append(int(input()))

    #condicionales para tipo de iva

for j in range(N):
    valor_producto.append(cantidad_producto_compra[j]*valor_unitario.get(codigo_de_produc[j]))
    if tipo_iv[j]==1:
            iva.append(0)        
    elif tipo_iv[j]== 2:
        iva.append(valor_producto[j]* 0.05)      
    else:
        iva.append(valor_producto[j]*0.19)
    valor_final.append(valor_producto[j]+iva[j])
    total_iva+=iva[j]
    total_ventas+=valor_final[j]

ordenamiento_burbuja(codigo_de_produc,cantidad_producto_compra,valor_unitario,iva,nombre_de_produc,valor_producto,valor_final)

i=0

for i in range(N):
    print(codigo_de_produc[i])
    print(articulos.get(codigo_de_produc[j]))
    print(valor_producto[i])
    print(valor_final[i])

print(total_ventas)
print(total_iva)