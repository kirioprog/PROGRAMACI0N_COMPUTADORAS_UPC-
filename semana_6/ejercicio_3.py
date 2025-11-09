# -*- coding: utf-8 -*-
import random
dic_alumnos = {}
cant_alumnos = int(input("Numero de alumnos: "))

for idx in range(1,cant_alumnos + 1):
    nombre = input(f"Ingrese nombre {idx}:")
    print(f"{nombre} - Notas:")
    print("------------------")
    #asignamos al alumno 5 notas aleatorias 
    dic_alumnos[nombre] = [random.randint(0, 20) for idx in range(0,5)]

   #utilizamos el enumerate para desempaquetasr la lista 
    for idx, notas in enumerate(dic_alumnos[nombre], start = 1):
        print(f"Quiz{idx}: {notas:0>2}")
        
    print()
    