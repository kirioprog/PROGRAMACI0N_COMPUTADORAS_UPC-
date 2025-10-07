# -*- coding: utf-8 -*-
import random 
nombres = []
codigo = []
for cant in range(0,5):
   nombres.append(input(f"Nombre de la persona {cant +1}: "))
   
   #genera un codigo aleatorio 
   nuevo_codigo = random.randrange(10,99)
   #preguntas si ese codigo nuevo aleatorio ya pertecene al la lista codigo , si ya pertence entonces entrara al bucle y parara cuadno nuevo_codigo no pertenezca a codigo 
   while nuevo_codigo in codigo :
       nuevo_codigo = random.randrange(10,99)
       
    #agregamos nuebvo_codigo a la lista 
   codigo.append(nuevo_codigo)
       
   

for cant, people in enumerate (nombres) :
    print(f"{people:<10}:  {codigo[cant]}")