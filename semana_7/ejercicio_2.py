# -*- coding: utf-8 -*-
import os



with open("notas.txt", mode = 'r', encoding='utf-8') as file:
    for idx in file :
        nombre,n1,n2,n3,n4,n5 = idx.strip().split(",")
        
        n1,n2,n3,n4,n5 = map(int,(n1,n2,n3,n4,n5))
        promedio = (n1 + n2 + n3 + n4 + n5) / 5
        
        print(nombre)
        
        print(f"Promedio: ({n1} + {n2} + {n3} + {n4} + {n5}) / 5 = {promedio:.1f}\n")