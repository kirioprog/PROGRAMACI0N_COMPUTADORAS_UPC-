#LISTAS Y TUPLAS 

#%%
##LIBRERIA MATH 
#==============


import math 

# si ejecutamos dir(math) en la terminal podremos ver todas las funciones disponibles en la biblioteca math 

#si queremos consultar como se utiliza una funcion colocamos en la terminal math.sin? esto aplica para la funcion sin 

math.sin(1)

#esto no es valido 
#   math.sin(x = 1)

#%%
#IMPORTAR LIBRERIA CON ALIAS 
    
#Esto nos sirve para ya no estar escribiendo a cada rato math.sin() sino solo vamos a escribir nombre_alias.sin()


import math as m

#para bucar como se utiliza una funcion es com9o el caso anterior, solo que ahora vamos a escribir m.sin? 
m.sin(1)

#%%IMPORTAR FUNCIONES EN ESPECIFICA 

from math import sin, cos, tan
#buscar ayuda en el terminal cuando importo funciones independiente, ingreso en la terminal sin ? y listo jeje

sin(1)

#%% 
#EJEMPLOS PRACTICOS CON LA BIBLIOTECA MATH

#TODO CON ESTO IMPORTAMOS TODAS LAS LIBRERIAS y solo basta con poner el nombre de la funcion y listo pero no es lo recomendado , es mejor poner alias
from math import *
m = 10
#=====================
print("1.4 elevada a la -3", 1.4e-3)
#para imprimir el pi observa que estamos utilizando el alias que anteriormente ya habiamos declarado 
print("PI =", m*pi)

#EXPRESIONES EXPONENCIALES Y LOGARITMICAS 
print("3**2", pow(3, 2))
print("raiz de 2", sqrt(2))
print("log(100)",log10(100))
#si escribes log en automatico python  reconoce como logaritmo neperiano
print("Ln(100", log(100))

print("log2(16)", log2(16))

#FUNCIONES TRIGONOMETRICAS 
print("sin(pi/4", sin(pi/4))
 #ingresas los valores de los catetos 
print("arcotan(5/4)", atan(5/4))

#convertir grados sexagesimales a radianes
print("pi/2", radians(90))
print("sin(pi/4)", sin(radians(45)))
#asin halla el arcosenoss de 0.707 y degrees convierta el resultado DE RADIANES A SEXAGESIMALES 
print("arcsin(0.707) radianes", degrees(asin(0.707)))

#REDONDEO DE NUMEROS 
#obtener la parte entera de cualquier numero 
print("la parte enterea de 1.73948", trunc(1.72948))
#Redondear hacia abajo
print("El redondeo hacia abajo de 4.98", floor(4.98))
#Redondeo hacia arriba
print("El redondeo hacia arriba de 3.01", ceil(3.01))


#%%
#todo TUPLAS
#=======================
#ES COMO UNA MATRIX PERO CON VALORES  CONSTANTES  PERO OJO QUE EN LA TUPLA PUEDES AÑADIR DATOS DE DIFERENTE TIPO 
t1 = (0,1, 2, 3, 4, 5)
t2 = (0, 'Uno', 'one', 1+0j)
#esta es una tupla de tuplas 
t3 = (t1, t2)
#aqui estas colocando la tupla 2 en la posicion 1 de la tupla 4, cuando se imprima se va imrpimir toda la tupla 2
t4 = (1, t2, 'A', t2, t3)
#todo el range genera una secuencia de 0 al 9 y esto los convierte en una tupla que sera llamada t5
t5 = tuple(range(10))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

#%%
#CREAR UN RANGO PARA LOS #todo  INDICES DE LAS TUPLAS 

#   [i_inicial: i_final + 1: paso_entre_indices] 
print(t1[0:3])
print(t1[ -1:-3:-1])
#va a ir desde el final hasta el inicio 
print(t1[::-1])
#imprime toda la tupla en orden 
print(t1[::])

#RETOMAR LA LONGITUD DE UNA TUPLA
len(t1)

#OTRAS OPERACIONES SE HACEN COMO UNA MATRIZ POR EJEMPLO
print(t3[0][0])

#%%
#todo DESEMPAQUETAMIENTO DE TUPLAS 

#estamos repartiendo la tupla en las variables a, b, c en ese orden 
a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)#%%
#todo TUPLAS COMO ITERABLES 
#Osea pueden ingrear a un for y este extraera sus elementos 
for number in(1, 2, 3, 4, 5):
    print(number)
print()
for idx in range(0, len(t1), 2):
    print(t1[idx])
    
#%%
#todo OPERACIONES CON TUPLAS

#SUMA DE TUPLAS
#Lo que va a pasar es que va añadiendo todo esto en una nueva tupla 
(1, 2, 3) + (4, 5, 6)
#%%
#Producto de tupla por un entero 
#Osea vamos a repetir la tupla 3 veces
(1, 2, 3) * 3 

#%%
#FUNCIONES UTILES CON TUPLAS 

t1 = (1, 4, 8, 12, 9, 5, 3)
#te b rinda la longitud de una tupla 
print(len(t1))
#encuentra el valor mas pequeño de una coleccion (tienen que ser del mismo tipo )
print(min(t1))
#Encuentra el valor mas grande de la coleccion 
print(max(t1))
#todo Ordena la coleccion
print(sorted(t1))
#Suma todos los elementos de la coleccion 
print(sum(t1))
#%%

#USO DE ELEMENTOS PARA DETECTAR TRUE O FALSE EN UNA TUPLA
#si uno de los elementos es true, devuelve true 
#RECUERDA: 0 ES FALSE Y TRUE TODO DIFERENTE DE 0 
print(any(t1))

#devuelve true si todos sus elementos son true
print(all(t1))


#%%
#todo LISTASSSSSSSSSSSSSSSSSSSS
#=========================================

#Las listas son como tuplas pero los elementos de estas si son modificables 

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = ['1', 'one', 1+3j]
#lista de lista 
L3 = [L1, L2, 'aqui estoy']
#todo genera una secuencia de numero de 0 a 9, los convierte en una lista cuyo nombnre sera L4 
L4 = list(range(10))
#es lo mismo que el anterior solo que lo convierete a tupla y de tupla a lista 
L5 = list(tuple(range(20)))
L6 = [1, 2, ['A', 'B'], ('a', 'b')]


print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(L6)
print(type(L1))

#%%

#AL IGUAL QUE UNA TUPLA LA LISTA ACEPETA VALORES POSITIVOS Y NEGATIVOS, SU INDICE FUNCIONA IGUAL 
print(L6[0])
print(L6[-1])
print(L1[1:7:3])
print(L6[2][1])
#%%
#LAS #todo OPERACIONES ENTRE LISTAS FUNCIONAN  IGUAL QUE EN LAS TUPLAS

print(L1 + L2)
#repite la lista 3 veces 
print(L1 * 3)
 
#TAMBIEN PUEDEN INGRESAR A UN BUCLE FOR 
for item in L1:
    print(item)

#%%
#todo ENUMERATE Y ZIP FUNCIONA PARA TUPLAS Y PARA LISTAS, ANBOS SE UTILIZAN CON UN FOR

#ENUMERATE
#Retorna una secuencia enumerada en tuplas de la forma(indice, elemento) 

#por defecto el star o numero inciial es 0

for item in enumerate(['A', 'B', 'C']):
    print(item)
    
idx = 0
for vocal in ['a', 'e', 'i', 'o', 'u'] :
    #estamos  diciendo que imprima el numero idx  + 1 y la pues la vocal que se imprime es la que ubicacion 0, todo se imprime en orden 
    print(f"{idx + 1}: {vocal}")
    idx +=1
    
print()
#PERO EL CODIGO ANTERIOR ESTA MAL ESCRITO PORQUE PYTHON PREFIERE LO PLANOP

#se acomodan entre extremos letras con enumerate y idx con start
#se ejecuta hasta llegart al ultimo elemento de la lista o tupla 
for idx, letras in enumerate(['a', 'b', 'c', 'd'], start = 1): 
    print(f"{idx}: {letras}")

#ZIP

#Extrae los elementos correspondientes de varias listas en simultaneo 
#zip(iterable1, iterable2)
#es como el enumarate pero con esteroides
nombres = ['Ana', 'Maria', 'Carlos']
edades = [23, 50, 18]

#Asigna respectivamente 
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
    
 #%%    
#todo M0DIFICAR LISTAS 

l = [1, 2, 3, 4, 5, 'A', 'A']
#APPEND()
#nos sirve para agregar un elementos al final de la lista 
#estamos añadiendo 6 al final de la lista, no se puede poner dentro del print porque append no retorna nada
l.append(6)
print(l)
print(l.append(6))

#INSERT(ubicacion, valor), inserta un valor en la ubicacion designada, NO RETORNA NADA
l.insert(1,'A')
print(l)

#POP: Extrae un valor en una ubicacion especifica  y lo elimina, RETONA ese vaLOR ELIMINADO
#elimino el valor de la ubicacion 2 y lo retorna !!!
print(l.pop(2))
print(l)
#REMOVE: Elimina un valor de la lista, si hay variois iguales elimina el primero que encuntra
l.remove('A')
print(l)


#CLEAR: elimina todos los elementos de la lista, tampoco retorna nada 
l.clear()
print(l)

l = [1, 2, 3, 4, 5]
#COPY: copia TODOS los elementos de una lista en otra 

new_l = l.copy()
print(new_l)

#SORT(): ordena los elementos de una lista  y no retorna nada 
l2= [5,7,3,7,2,0]
l2.sort()
print(l2)

#SORTED: RETORNA nada,a ordenas los elementos pero en una nueva lista 
l2 = [5,7,3,7,2,0]
sorted(l2)
print(l2)
print(sorted(l2))

#EXTEND: AGREGA TODOS LOS ELEMENTOS DE UNA LISTA EN EL FINAL DE OTRA 
 #agreadamos a, c,, b al final de la lista l 
l.extend(['a','c','b'])
print(l)

#%%
#TODO LISTAS POR COMPRENSION

#ESTE ES UN EJEMPLO NORMAL 
lista = []
for num in range(1, 10):
    lista.append(num)
    
print(lista)

#CON UNA LISTA POR COMPRESION ES MEJOR 

#[<expresión> for <variable> in <secuencia>]
#expresione es el valor que se guarda en la lista
#variable es el valor temporal a cada elemento de la lista 
#la expresion y variable tiene que tener el mismo nombre    

#lista será igual a los numeros para todos los numeros en el rango de 1 a 9"
lista = [num for num in range(1, 10)]
print(lista)
