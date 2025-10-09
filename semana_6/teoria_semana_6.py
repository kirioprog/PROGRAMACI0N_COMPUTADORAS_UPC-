# CONJUNTO
#en un conjunto los elementos que la conforman no tiene un orden en especifico y estos solo se pueden repetir una sola vez en el conjunto 
conjunto: set = {1, 2, 3, 4, 5, 2,  6, 7, 8}
print(conjunto)
#%%
#todo convertir una lista en conjunto 
set([1,2,3,4,5, 6])
#%%
#TODO LOS CONJUNTOS SON ITERABLES 

num = input("Ingrese un numero entero: ")

numeros = set([n for n in num])
#no que trato de hacer el profesor pero bueno xd 
if len(num) == len(numeros):
    print("Digitos diferentes")

else:
    print("Hay digitos repetidos")
    
#%%
#todo obsefvasr los metodos disponibles son conjuntos (set )
dir(set)
#%%
#todo Creamos un conjunto vacio para agregar los elementos  
s = set()
#voy agregar los elementos utilizando add, recuerda que en un cojnunto los elementos no tienen orden por ello no se van agregar en ese orden especificaamente 
s.add(0)
s.add(1)
s.add(4)  
s.add(10)
print(s)
#%%
#todo descartar elementos de un conjunto 
#entre los parentesis voy a colocar los elemkentos que voy a descartar de mi conjunto 
s = {3,433,10,67,4,4,4,}
s.discard(4)
s.discard(10)
print(s)
#%%
#todo extraer un valor aleatorio de mi conjunto 
#lo vamos hacer con pop, dice que es aleatorio porrque como los elementos no tienen un orden especifico por ello.  
s = {3,33,10,67,4,4,4,}
val: int = s.pop()

print(" Valor aleatorio es : ",val)

print(s)

#%%
#TODO OPERACIONES CON CONJUNTOS 

pares = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
mult_3 = {0, 3, 6, 9, 12, 15, 18, 21}
mult_5 = {0, 5, 10, 15, 20, 25}

#interseccion : que imprima lo s numeros que son pares y multiplos de 3 
print(pares & mult_3)
#Union: que impiram los numeros que son multiplos de 5 o multiplos de 3 
print(mult_5 | mult_3)

#Diferencia  : imprima los elemenots que son pares  y quita os que son multiplos de 3 
print(pares - mult_3)

#todo Diferencia simetrica : imprima los multiplos de 3 y multiplos de 5 pero no aquellos que son ambos al mismo tiempo 
print(mult_3 ^ mult_5)
#%%
#LOS CONSJUNTOS SON ITERABLES OSE ALOS PUEDDO UTILIZASRT CON UN BUCLE FOR 
print()
for element in {1,2 ,3 ,4 ,5, 5}:
    print(element)
    #%%

#VAMOS A CREAR UN JUEGO DE LOTERIA 

from random import randint 

#creamos una funcion que tiene como parametro n_bolos y n_sorted de tipo entero  y nos va a devcolver una lista de numeros enteros 

def sorteo (n_bolos: int, n_sorted: int) ->list[int]:
    if n_sorted > n_bolos :
        #creamos una excepcion que nos dejara el sieguiente mensaje 
        raise ValueError("El numero de bolas supera el numero de sorteos")
    
    sorteo = set()
    while len(sorteo) < n_sorted:
        sorteo.add(randint(1,n_bolos))
    else:
        return list(sorteo)

#llamemos a la funcion para ver si funcion a

sorteo(24,8)
sorteo(8,25)

#%%DICCIONARIOS
#llave : objeto 
#considera la llave como tu indice, es casi la misma idea 
#los diccionarios no tienen indice 
diccionario: dict = {'python': 1991, 'c': 1972, 'java':1996}

print(diccionario)
print("numero de elementos", len(diccionario))
#%%
#agregar un elemento al diccionario 
d = {}
d['python']= 2001
d['c++']= 1983
d['javascrip'] = 1995
print(d)
  

#%%
#que nos arroje el valor de una llave 
print()
diccionario['c']
print("el valor de año en que se creeo python es:", diccionario['c'])

#%%
# El diccionario 'persona' almacena cada dato de una persona en llaves
persona: dict[str, str] = {'nombre': 'Elvio',
                           'apellido': 'Lado',
                           'edad': 20,
                           'telefono': '976-765-262',
                           'direccion': 'Av. Separadora Industrial 2134, Ate'}

print(persona)
print()
print(persona['nombre'] + ' ' + persona['apellido'])

#ahora supongamos que queremos cambiar el tefelono de la persona
persona['telefono'] = '983-343-432'
print(persona)

#%%
#DICCIONARIO COMO UN ITERABLE 
meses = {1: 'ene', 2: 'feb', 3: 'mar',
                         4: 'abr', 5: 'may', 6: 'jun',
                         7: 'jul', 8: 'ago', 9: 'set',
                         10: 'oct', 11: 'nov', 12: 'dic'}

#keys retorna una lista con todas las llaves del diccionario 
for item in meses.keys():
    print(item)

#Values retorna un alista con ltodos los valores del diccionario 
for item in meses.values():
    print(item)
    
#items retorna una tupla con todos los pares (llave, valor)
for item in meses.items():
    print(item)



#%%
#metodos de un diccionario 
dir(dict())
#%%
meses = {1: 'ene', 2: 'feb', 3: 'mar',
                         4: 'abr', 5: 'may', 6: 'jun',
                         7: 'jul', 8: 'ago', 9: 'set',
                         10: 'oct', 11: 'nov', 12: 'dic'}
#extraer el valor de un diccionario a partir de una llave 
val = meses.pop(10)
print(val)
print(meses)
#%%
#retorna el valor de una llave, pero si un caso esa llave no existe como la llave 10 entonces puede retornar el mensaje que tu le asignes 
meses.get(10,'no hay')

#creamos un diccionario a partir de 2 listas, como puedes observar una lista es para las llaves y otra para los valores 

#TODO ESTO CON LA FUNCION ZIP 
meses_n: list[str] = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 
                      'jul', 'ago', 'set', 'oct', 'nov', 'dic']
meses_d: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

meses = dict(zip(meses_d, meses_n))
print(meses)

#%%
#  DICCIONARIOS POR COMPRESION 

#Vamos a crar un diccionarios que relacione grados centigrados a grados Fahrenheit 

#creamos la variable c_to_f el cual es un tipo de variable diccionario con llave de tipo int y valores de tipo float 


c_to_f: dict[int, float] = {c: round(9/5 * c + 32, 1) for c in range (20,31)}
print(c_to_f)

#%%

#Tambien podemos utilizar in para verificar si una llave se encuentra en el diccionario 

print(3 in meses)

#ojo : enero es un valor no es un a llave asi que como llave enero no se encuentra en meses 
print('enero' in meses)
#%%

#LISTAS EN  UN DICCIONARIO 

leng_prog = {'juan': ['Python'],
             'maria': ['C', 'C++'],
             'elvio': ['HTML', 'JavaScript', 'PHP'],
             'clodoaldo': ['Assembler', 'Haskell'],
             'rosa': ['Python', 'VisualBasic']
             }

# El lazo for extrae los pares (llave, valor) con el metodo items()
for nombre, lenguajes in leng_prog.items():
    #recuerda que capitalize convierte el primer caracter en mayuscula y el resto en minuscula 
    print(f"Lenguajes favoritos de {nombre.capitalize()}:")
    
    for idx, lenguaje in enumerate(lenguajes, start= 1):
        print(f"\t {idx} {lenguaje}")
    else:
        print()
        
#%%
#DICCIONARIO EN LISTAS 

# alumnos[0]['apellido']
alumnos = [{'nombre': 'Elvio',
            'apellido': 'Lado',
            'codigo': 'A8383783',
            'email': 'elado@yahoo.com',
           },
           {'nombre': 'Maria',
            'apellido': 'Jimenez',
            'codigo': 'A8309806',
            'email': 'mjimenez@mail.com',
           },
          ]

for idx, alumno in enumerate( alumnos, start = 1):
    print("Alumno:", idx)
    #recuerda que items saca pares de valores
    for m, n in alumno.items():
        print(f"{m.capitalize()}: {n}")
        
    else:
        print()
        
#%%
#DICCIONARIOS EN DICCIONARIOS 
alumnos = {'elazo': 
                {'nombre': 'Elvio',
                'apellido': 'Lado',
                'codigo': 'A8383783',
                'email': 'elado@yahoo.com',
                'telefono': {'movil': '987-345-222',
                             'fijo': '245-3783',
                            }
                },
           'mjimenez': {'nombre': 'Maria',
                'apellido': 'Jimenez',
                'codigo': 'A8309806',
                'email': 'mjimenez@mail.com',
                'telefono': {'movil': '918-727-272',
                            }
               },
          }
    
for  username, user_info in alumnos.items():
    print("\tNOMBRE DE USUARIO:", username)
    print(f"\tNombres: {user_info['nombre']} {user_info['apellido']} ")
    print(f"\tCODIGO: {user_info['codigo']}")
    print(f"\tCORREO ELECTRONICO: {user_info['email']}")
    print()