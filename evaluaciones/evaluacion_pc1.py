# -*- coding: utf-8 -*-
def totalPalabras(texto: list) ->int:
    total = len(texto)
    return total

def palabrasUnicas(texto: list) ->int:
    conteo = 0
    for idx in range(0,len(texto)):
        if texto.count(texto[idx]) == 1:
            conteo +=1
            
    return conteo
            
#%%
def longPromedio(texto):
    """Retorna la longitud promedio de las palabras"""
    palabras = texto.split()
    if len(palabras) == 0:
        return 0
    
    suma_longitudes = sum(len(palabra) for palabra in palabras)
    promedio = suma_longitudes / len(palabras)
    return promedio
#%%

def palabraCortaLarga(texto: list):
    palabra_larga = ""
    palabra_corta = ""
    
    for idx in range(0,len(texto)):
        if len(texto[idx]) > len(palabra_larga):
            palabra_larga = texto[idx]
    for idx in range(0,len(texto)):
        if len(texto[idx]) < len(palabra_corta):
            palabra_corta = texto[idx]
            
    return palabra_larga, palabra_corta

#%%
def freqVocales(texto):
    """Retorna un diccionario con la frecuencia de cada vocal (a, e, i, o, u)"""
    texto_lower = texto.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    frecuencias = {}
    
    for vocal in vocales:
        frecuencias[vocal] = texto_lower.count(vocal)
    
    return frecuencias

#%%
texto_final= input("Ingrese un texto: ").split()
print(texto_final)

print("Numero total de palabras : ", totalPalabras(texto_final))
print(f"Numero total de palabras Unicas: {palabrasUnicas(texto_final)}")
print(f"La palabra mas larga del texto es: {palabraCortaLarga(texto_final)[0]}")
print(f"La palabra mas corta del texto es: {palabraCortaLarga(texto_final)[1]}")