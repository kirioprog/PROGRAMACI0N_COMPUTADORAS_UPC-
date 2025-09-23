# -*- coding: utf-8 -*-

print()
#EL CODIGO ESTA CENTRADO EN UN ESPACIO DE 62 CARACTERES 
print(f"{'LISTA DE COMPRAS':^62}")
print(f"{'================':^62}")
print()

# la palabra PREC TOTAL ocupa 9 espacios
print(f"{'CANTIDAD':<10} {'DESCRIPCION':<23} {'PREC UNIT':<11} {'PREC TOTAL'}")
print(f"{'--------':<10} {'-----------':<23} {'---------':<11} {'----------'}")

#LISTAS
cantidad = [4, 7, 3, 1 ,4]
producto = ["Leche", "Arroz", "Azucar", "Gaseosa", "Galleta"]
#TUPLA
prec_unitario = (4.2, 3.8, 4.5, 3.5, 1.0)
total = 0

#anidar f-string

#El f-string siempre esta entre " " o ' ' 
total_producto= prec_unitario[0] * cantidad[0];       total += total_producto
print(f"{f'{cantidad[0]:0>2}':^10} {producto[0]:<23} {prec_unitario[0]:>5.2f} PEN   {total_producto:>5.2f} PEN")

total_producto= prec_unitario[1] * cantidad[1]; total += total_producto
print(f"{f'{cantidad[1]:0>2}':^10} {producto[1]:<23} {prec_unitario[1]:>5.2f} PEN   {total_producto:>5.2f} PEN")

total_producto= prec_unitario[2] * cantidad[2]; total += total_producto
print(f"{f'{cantidad[2]:0>2}':^10} {producto[2]:<23} {prec_unitario[2]:>5.2f} PEN   {total_producto:>5.2f} PEN")

total_producto= prec_unitario[3] * cantidad[3]; total += total_producto
print(f"{f'{cantidad[3]:0>2}':^10} {producto[3]:<23} {prec_unitario[3]:>5.2f} PEN   {total_producto:>5.2f} PEN")

total_producto= prec_unitario[4] * cantidad[4]; total += total_producto
print(f"{f'{cantidad[4]:0>2}':^10} {producto[4]:<23} {prec_unitario[4]:>5.2f} PEN   {total_producto:>5.2f} PEN")

print()
print("-" * 58)
print()
print(f"{'':10} {'SUB TOTAL   :':<8} {total:>27} PEN")
print(f"{'':10} {'IGV [18%]   :':<8} {total * 0.18:>27} PEN")
print(f"{'':10} {'TOTAL + IMP :':<8} {total * 0.18 + total:>27} PEN")


#print(f"{'hola':->10}")
#va ocupar 10 caracteres de los cuales utiliza 4 para poner hola en la parte derecha y el resto lo ocupa con -
