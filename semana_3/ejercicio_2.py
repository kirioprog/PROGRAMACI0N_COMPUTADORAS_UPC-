# ñ-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random

# Generar lista inicial de 6 números enteros de 2 dígitos
# "Toma un número aleatorio entre 0 y 99 y hazlo 6 veces (una por cada value de 0 a 5), guardando todos esos números en una lista."
lista_original = [f"{random.randrange(0,99):0>2}" for value in range(6)]
print(lista_original)

#LISTA NUEVA
#RECUERDA : FOR FOR ES COMO SI ESTUVIERA UN FOR DENTRO DE OTRO FOR, EL PRIMER FOR TIENE MAS JERARQUIA Y ASI SUCESIVAMENTE
#para cada numero de la lista original, si numero es par el for tendra una longitud de 2 en donde sera numero y 00 y como observas ese valor es el que se agrega a lista actualizada pero si es imrpar ese for tendra una longitud de numero y ese valor se añadre
lista_actualizada = [elemento for numero in lista_original for elemento in ([numero, '00'] if int(numero) % 2 == 0 else [numero] ) ]
print(lista_actualizada)

lista = ['ave', 5]
for idx in lista:
    print(idx)