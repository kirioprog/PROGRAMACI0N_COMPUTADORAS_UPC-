# -*- coding: utf-8 -*-
import random 
n = int(input("Inserte la cantidad de alumnos: "))

#otra manera de hacerlo 
#nombres = []
#for idx in range(n):
  #  nombres.append(input(f"Alumno {idx +1}: ")) 
#print(nombres)
    
nombre = [input(f"Alumno {idx +1}: ") for idx in range(n)]
#de verificacion
#print(nombre)

notas = []

for idx in range(n):
   notas.append([random.randrange(0,20) for can in range(5)])
   print(f"{nombre[idx]}",*notas[idx],sep=(', '),end = '')
   print("|", end = '')
   
   