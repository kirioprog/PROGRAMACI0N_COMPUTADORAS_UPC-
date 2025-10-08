# -*- coding: utf-8 -*-
def aprobados(notas: list) -> list:
    
    notas_aprobadas = list(filter(lambda x: x >= 13, notas))
    return notas_aprobadas 

notas = [18, 15, 10, 12, 16.5, 20, 11]
print("Las notas aprobadas son: ", aprobados(notas))