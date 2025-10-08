# -*- coding: utf-8 -*-
def eliminar(frase: str) ->str:
    frase_final: str = ""
    #cambiamos todas las "a" por "A"
    frase_mayu= frase.replace("a","A")
    #una vez modificado las "a" podemos contar cuantas "A" hay en la frase 
    m = frase_mayu.count("A")
    
    
    nueva_frase = [frase_mayu[idx]for idx in range(0,len(frase))]
    
    #eliminamos todas las A de la nueva frase
    for cantidad in range(0,m):
        nueva_frase.remove("A")
        
    #Amamos nuestra str a partir de la lista 
    for lon_final in range(0,len(nueva_frase)):
        frase_final += nueva_frase[lon_final]
    
    
    return frase_final


frase = input("Ingrese una frase: ")

print(f"Frase procesada: {eliminar(frase)}")

