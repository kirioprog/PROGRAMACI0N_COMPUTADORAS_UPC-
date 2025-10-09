# -*- coding: utf-8 -*-
def totalPalabras(texto: str) ->int:
     longitud = len(texto)
     return longitud 
 
def palabrasUnicas(texto: str) ->int:
    conteo = 0 
    for idx in range(0,len(texto)):
        if texto.count(texto[idx]) == 1:
            conteo +=1
    return conteo 

def longPromedio(texto: str) ->float:
    cantidad = len("".join(texto))
    n_palabras = len(texto)
    long_promedio = cantidad / n_palabras
    return long_promedio 
    
def palabraCortaLarga(texto: str):
    palabra_corta = min(texto)
    palabra_larga = max(texto)
    return palabra_corta, palabra_larga



#%%
texto_final = input("Ingrese un texto: ").split()

while len(texto_final) == 0:
    texto_final = input("Ingrese un texto: ").split()
    

print()
print(f"Numero total de palabras: {totalPalabras(texto_final)}")
print(f"Numero de palabras unicas: {palabrasUnicas(texto_final)}")
print(f"Longitud promedio de las palabras: {longPromedio(texto_final)} ")
print(f"La palabra mas corta es: {palabraCortaLarga(texto_final)[0]}")
print(f"La palabra mas larga es: {palabraCortaLarga(texto_final)[1]}")



