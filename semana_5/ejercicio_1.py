# -*- coding: utf-8 -*-

def creaCadena(cadena):
    vocales = "aeiouAEIOU"
    nueva_str = ""
    for letra in cadena.strip() :
        if letra in vocales :
            nueva_str += letra
        
        
    return  nueva_str
    

cadena = input("ingrese una frase: ")
print(f"cadena formada:{creaCadena(cadena):}")