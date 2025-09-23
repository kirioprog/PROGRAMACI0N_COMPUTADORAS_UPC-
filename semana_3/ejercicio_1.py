# -*- coding: utf-8 -*-
valores = []
#pedir los numeros
for cuenta in range(10):
   valores.append(float(input(f"Ingrese numero {cuenta + 1:<3}: ")))
    
#imprimir la lista con todos los valores 

print("\n\nNumeros reales")
#utilizas range(len) par que te genere numeros en un rango de 0 hasta longitud de la lista
for cuenta, list_one in enumerate(valores, start = 1):
    print(f"numero {cuenta:<3} : {list_one:>10.2f}")
    
#LISTA DE VALORES QUE PERTENECEN AL INTERVALO 
#si el elemento pertenece al rango se imprime 
print("\n\nNumeros que pertenecen al intervalo")
#en vez de poner toda la lista solo pongo el nombre de la lista la cual es valores , en mi caso valores tiene 10 elementos entonces el for se ejecutara 10 veces y cada vez con un elemento diferente 
for item_2 in valores:
    if 20 <= item_2 <= 60 :
        print(item_2)
        