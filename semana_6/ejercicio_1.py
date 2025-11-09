# -*- coding: utf-8 -*-

frase = input("Ingrese una frase: ")
#recoerdar que .upper es para convertir todo el str a mayuscula 
sentence_new = frase.strip().upper()
persona: dict[str,int] = {'A': 0,'E': 0,'I':0 ,'O':0 ,'U': 0}

for vocal in persona.keys():
    #recordar que .count es para contar cuantas veces se repite un str
    persona[vocal] = sentence_new.count(vocal)
    print(f"{vocal}: {persona[vocal]}")