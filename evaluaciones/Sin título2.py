# -*- coding: utf-8 -*-
def palabraCortaLarga(texto):
    """Retorna tuplas con todas las palabras más cortas y más largas"""
    palabras = texto.split()
    
    if len(palabras) == 0:
        return ([], [])
    
    # Encontrar longitudes mínima y máxima
    long_min = len(min(palabras, key=len))
    long_max = len(max(palabras, key=len))
    
    # Encontrar TODAS las palabras con esas longitudes
    palabras_cortas = [p for p in palabras if len(p) == long_min]
    palabras_largas = [p for p in palabras if len(p) == long_max]
    
    return (palabras_cortas, palabras_largas)

# OPCIÓN 1: No usar .split() en el input
texto_final = input("Ingrese un texto: ")  # ← SIN .split()
print(f"La palabra mas corta del texto es: {palabraCortaLarga(texto_final)[0]}")
print(f"La palabra mas larga del texto es: {palabraCortaLarga(texto_final)[1]}")