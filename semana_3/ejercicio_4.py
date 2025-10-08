# -*- coding: utf-8 -*-

# Lista de personas
lista_personas = ["Andrea", 18,
                 "Juan", 22,
                 "Arturo", 16,
                 "Manuel", 15,
                 "Daniela", 22,
                 "Renato", 24,
                 "Marcela", 22,
                 "Andres", 17,
                 "Carlos", 40,
                 "Sergio", 21,
                 "Tatiana", 33,
                 "Gisella", 36,
                 "Giancarlo", 17,
                 "Julio", 21,
                 "Pedro", 33]

print("Personas que pueden ir a la fiesta")

#observa que los nombres son numertos pares y las edades pares
lista_nombres =[lista_personas[nombre] for nombre in range(0,len(lista_personas), 2)]

lista_edades = [lista_personas[edad] for edad in range(1,len(lista_personas) , 2)]

for nombre,edad in zip(lista_nombres, lista_edades):
    if edad >= 18:
        print(f"{nombre:<10}: {edad}")
        
        
