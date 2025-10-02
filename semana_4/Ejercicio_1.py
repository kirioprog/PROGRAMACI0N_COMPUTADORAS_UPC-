# -*- coding: utf-8 -*-


def triangulo(lado1, lado2, lado3):
    valor_absoluto = abs(lado2 - lado3)
    if valor_absoluto < lado1 < (lado2 + lado3):
        return True
    return False 


#al ser varios valores los que ingresaremos con map los podemos serparar y convertir a int cada uno de estos 
lado1, lado2, lado3 = map(int, input("Ingrese los valores de un triangulo: ").split())

if triangulo(lado1, lado2, lado3) == True:
    print("El triangulo existe")
else:
    print("El triangulo no existe")
    
    
    