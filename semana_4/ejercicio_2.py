# -*- coding: utf-8 -*-


def max_min(one, two, three, cuatro, five):
    lista = [one, two, three, cuatro, five]
    
    print("el numero maximo es :", max(lista))
    print("el numero minimo es:", min(lista))  

#colocamos el map para que lo convierta en 
lista = list(map(int, input("ingrese 5 valores enteros para hallar el max y min ").split()))
#recuerda que el * desempaqueta una lista o una tupla 
max_min(*lista)



  