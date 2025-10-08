# -*- coding: utf-8 -*-

#%%
num = 10 
if num > 5:
    print(f"{num} es mayor a 5")
    
print("FINALIZAMOS")

#%%
num = 2 
if num <= 5:
    print(f"{num} es menor o igual a 5")
else:
    print(f"{num} es mayor a 5")

#%%
num = 15 
print(f"el numero {num}")

if num % 2 == 0:
    print("el numero es divisible entre 2 ")
elif num % 3 == 0:
    print("el numero es divisible entre 3")
elif num % 5 == 0:
    print("el numero es divisible entre 5 ")

#%%

#TODO convertimos la entrada de imput a entero 
anio = int(input("Ingrese el año : "))

# si el año es multiplo de 4 puede ser bisiesto 
if anio % 4 == 0:
    #le pongo pass porque si quiero escribir el eslse sin ningun relleno tengo que ponerlo 
    #pass
    #depende si termina en ..00
    if anio % 100 == 0:
        #.. a menos que sea multiplo de 400
        if anio % 400 == 0:
            print("ES BISIESTO")
        else:
            print("no es bisiesto")
    else:
        print("Es bisiesto")
else:
    print("No es bisiesto")

#%%
#TODO: PYTHON ODIA LO ANIDADO Y PREFIERE EN UNA (LINEA)(plano)
anio = int(input("INGRESE SU AÑO: "))

if anio % 4 == 0 and (anio % 100 != 0 or anio %400 == 0):
    print("Es biesto")
else:
    print("No es bisiesto")

#%%
lista = ["alicia", "jacinta", "susana", "maria"]
novia = "susana"


#TODO el operador "in" pregunta si argumento 1 esta dentro de argumento 2
print(novia in lista)
print(novia not in lista)
print ("jacinta" in lista)

#%%
num = int ( input("Ingrese un numero entre 1| y 10: "))

if num in [0, 2, 4, 8, 10]:
    print(f"{num} es par")
else:
    print(f"{num} es impar")

#%%%
#TODO RANGE 
#range genera un rango de datos 
#tiene 10 valores desde 0 hasta el 9
range(10)


#rango de 1 hasta 4
range(1, 5)
 
#cuenta de 1a 10 pero de 2 en 2 
range(1, 10, 2)  #1,3,5,7,9

#el paso por defecto es 1, asi que tienes que ponerle el paso -1 para que valla de 10 a 1
range(10, 1, -1)  #10,9,8....,2

#%%
#RECUERDA: IN SIGNIFICA ESTA ADENTRO DE 
5 in range(0, 20, 2)
#%%

num = int(input("Ingrese un numero positivo: "))

if num in range(0, num + 1, 2):
    print(f"{num} es par")
else:
    print(f"{num} es impar")

#%%
#TODO FOR 
number_list = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

#para cada numero que esta en la lista imprime, los elementos de la lista se guardan en each_number

for each_number in number_list:
    print(each_number)
    
#%%
print("Secuencia de numero pares ")

for num in range (0,21,2):
    print(num,end='--')
#%%
num_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 53, 57, 59]

print("Para todos los numeros impares entre 1 y 59, los numeros primos son:")
for num in range(1, 60, 2):
    if num in num_primos:
        print( " *", num)
else:
     print("Los demas numeros no son primos")
    

#%%
#todo while
num = 5
while num > 0:
    print(num)
    num -=1
#%%
#todo TRY - EXCEPT
#voy a intentar algo almenos de que salga algho mal 
edad = input("Ingrese su edad: ")
try:
    #como el codigo se ejecuta en orden si ingresar "quince" altoque te arooja error y te mand a excep 
#por ejemplo ingresas quince, esto no se puede convertir a int por lo tanto te manda a excep porque detecto ese error .
    edad = int(edad)
    if edad < 18:
        print("DNI AMARILLO")
    else:
        print("DNI AZULITO")
except:
    print("La edad ingresada no es valida")
    
#%%
#estos2 numeros etan separados por un /
try:
    n1, n2 = input("Ingrese 2 numeros n1/n2: ").split('/')
    print("los numeros son:", n1, n2)
    
    #si hay un error ese error se guarda en e y luego lo imprime
    #NO LE HAGAS MUCHO CASO A ESTO JEJE , ES MEJOR PONER TU PROPIO ERROR 
except Exception as e:
    print(e)
    

#%%
#TODO BREAK CONTINUE

#break sale del bucle

#continue omite todo lo que esta debajo y continua con su bucle 
num_valido = False
while not num_valido:
    try:
        num = int(input("Ingrese un numero entre 1 y 10: "))
    except ValueError:
        print("Debe ingresar un numero entero")
        continue  
    
    if num < 1 or num > 10:
        print("debe ser un numero entre 1 y 10")
    else:
        num_valido = True
        if num % 2 == 0:  
            print("es par")
            
        else:
            print("Es impar")
            
            
            
#%%
#else despues de un for par evitar confuncion al momento de leer 
#el else solo se ejecuta cuando se acaba todo el for, si lo rompes con un break, ya no se ejecuta

for num in range(10):
    print(num)
    
#lo que sucede justo despues de terminar el for 
else:
    print(num + 1)

#%%
#hacer comentarios reservados par hacer TODO
#todo el pass te permite ejecutar el codigo sin terminarlo 
if num < 0:
   
    pass
else:
   
    pass
#%%
#TODO MATCH ... CASE  
opc = int(input("Ingrese una opcion valida: "))

match opc:
    # si opc es 1 entonces se imprime opcion 1
    case 1:
        print("opcion 1")
    case 2:
        print("Opcion 2")
    case 3:
        print("Opcion 3")
    # este es como el else 
    case _:
        print("Opcion invalida")
#%%
#FORMA UTIL DE UTILIZAR MATCH CASE
cannot_exit = False     # Controla si la opcion 0 puede salir o no
opc = int(input("Ingrese una opcion válida: "))

match opc:
    case 1 | 2 | 3:    # Reconoce 1, 2 o 3
        print(f"Opcion {opc}")
    case 0 if not cannot_exit:    # Reconoce la opcion de salida si la salida esta habilitada
        print("Salir")
    case _:
        print("Opcion inválida")
 #%%
 #TODO RANDOM 
import random

# Para ver todas las funciones disponibles dentro de la librería random 
dir(random)

# Nos imprime información sobre la función random 
help(random.random)

# random() genera números entre 0.0 y 1.0
for i in range(5):
    print(random.random())

# RANDRANGE - retorna valores enteros aleatorios en un rango determinado 
for i in range(5):
    print(random.randrange(1, 10))  # enteros de 1 a 9

# UNIFORM - retorna un valor float aleatorio en un rango  
for i in range(5):
    print(random.uniform(1, 10))    # floats de 1.0 a 10.0