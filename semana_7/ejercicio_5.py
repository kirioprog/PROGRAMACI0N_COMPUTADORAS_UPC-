# -*- coding: utf-8 -*-
import os 
import csv 
import random

alumno = {}
for idx in range(0,10):
    nombre = input(f"Ingrese el nombre del alumno {idx}: ")
    alumno[nombre] = [random.randint(0, 20) for idx in range(0,6)]
    
    
    
    
with open('notas.csv', mode = 'w', encoding = 'utf-8', newline = '') as file :
    #VAMOS A CONTRAOLAR LAS FILAS Y EL DELIMITADOR 
    fila = csv.writer(file, delimiter = ';')
    #aHORA SI CREAMOS LOS ENCABEZADOS 
    fila.writerow(["Alumno","nota1","nota2","nota3","nota4","nota5","nota6"])
    
    #VAMOS A ESCRIBIR EN EL ARCHIVO 
    #recuerda que .items() te deuvel llave, valor 
    for nombre, notas in alumno.items():
        fila.writerow([nombre] + notas)
    
    
    
    