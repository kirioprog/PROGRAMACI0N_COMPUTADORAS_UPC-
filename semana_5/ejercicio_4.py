# -*- coding: utf-8 -*-

def revertir(palabra: str) ->str:
    nueva: str = ""
    for idx in range(len(palabra)-1,-1,-1):
        nueva += palabra[idx]
        
    
    return nueva

         
    
    
    
    
    
frase = input("Ingrese una frase: ").split()

#print(frase)

print("palabras al reves de la frase: ")

for idx in  range(0,len(frase)):
    print(revertir(frase[idx]))