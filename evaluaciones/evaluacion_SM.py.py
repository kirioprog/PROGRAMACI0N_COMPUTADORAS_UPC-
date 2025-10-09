# -*- coding: utf-8 -*-
#reto de profesor puerta
def palabras_s(palabra: str) -> str:
    longitud = len(palabra)
    if palabra[longitud - 1] == 's':
        return palabra 
    else:
        return''
    
def palabra_minus(palabra: str) ->int:
    nuevo_texto = palabra.lower()
    for idx in range (0,len(palabra)):
        if palabra[idx] == nuevo_texto[idx]:
            return 1
    return 0
#%%
contador: int = 0  
frase = input("Ingrese una frase: ").split()

print("\nPalabras con s al final: ")
for m in range(0,len(frase)):
    if palabras_s(frase[m]) != '': print(palabras_s(frase[m]))
    
for idx in range(0,len(frase)):
    contador += palabra_minus(frase[idx])
else:
    print(f"\nPalabras con almenos una letra minuscula : {contador}")
      
    
