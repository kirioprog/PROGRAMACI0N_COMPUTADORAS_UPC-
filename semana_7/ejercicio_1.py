# -*- coding: utf-8 -*-
import os
import random
with open("notas.txt", mode = 'w', encoding= 'utf-8') as file :
    nombres = {'juan':[],'pablo': [],'mercurio':[],'alan':[], 'toledo':[], 'castillo':[], 'Dina':[], 'Porky':[], 'Retiro':[], 'MANO':[]}
    
    for idx, nombre in enumerate(nombres, start = 1):
        nombres[nombre] = [random.randint(0, 20) for idx in range(0,5)]
        #con map convertimos la lista en string y con join los separamos mediante comas y desempaquetamos
        file.write(f"{nombre}, {', '.join(map(str, nombres[nombre]))}\n")
        
print(nombres)