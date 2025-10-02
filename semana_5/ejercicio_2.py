# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 10:47:57 2025

@author: danie
"""

frase  = input("Ingrese una frase: ")
letra = input("Ingrese  una palabra: ")
cantidad = frase.count(letra)
print(f'La palabra "{letra}" esta contenida {cantidad} veces en la frase')