# -*- coding: utf-8 -*-
import os 

import csv

nombre = "pais.csv"
with open(nombre, mode  = 'r', encoding = 'latin-1', newline = '') as file :
    # con este podemos extraer fila por fila 
    
    fila = csv.DictReader(file,delimiter = ';')
    
    for pais in fila :
        if int(pais['Puntos']) > 29 :
            print(pais['Pais'])
            
        
            

    
    
    