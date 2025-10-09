  #En este apartado vamos a ver la teoria de python
#%%
#imprimir mensajes utilizamos print
# %%
#podemos utilizar " o ' 
print("hello, word")
print('Hello, word')
print('hello, "word"')


#%%
#la , lo que hace es generar espacio en blanco
#escribiendo print? en el terminal puede consultar lo que pasa con print

print(1, 2, 3, 4, 5)
#TODO END  Y SEP     
#vamos hacer que el separador sea ->
#esto lo hacemos utilizando el argumento sep 
print(1, 2, 3, 4, 5, sep='->')

#con esto estamos cambiando el \n por ''
print(1, 2, 3, 4, 5, end= '')
print("hello word")
#%% 
#la funcion print automaticamente al final te añade el \n
print("hello word")
print("adios, mundo")
#%%
#pero si puedes utilizar el\n adentro de print para bajar una linea el mensaje

print("Hello word\nHola mundo")

#%%

#Operaciones Aritmericos
#------------------------------------------------------------
#Podes observas que no tienen  elementos de posicion
# solo pones dent4ro de las " lo que quiers que se imprima
#con la coma añades otro argumento que se va a imprimir el valor resultante
#enade 
print("2 + 3 = ",2+3)
print("3 - 6 = ", 3 - 6)
print("4 * 3 =", 4* 3)
print(" Division 3 / 2 =", 3 /2)
print("Divicion con redondeo al entero 3//2 =", 3 //2)
print("Pontencias 3 al cuadrado", 3 ** 2)
print("matematica de reloj 3 % 2 =", 3 % 2)

#%%
#VARIABLES
#---------------------------------------------------------
#En python no tienes que declarar variables ni tipos de datos
#en operaciones matematicas las reconoce automaticamente el tipo

#este retorna un entero porque la potencia siempre da un entero

print(2 **(6-3))

#este retorna un float porque la division siempre da un float 

print(2 **(6-1)/2)

a= 10
print(a)
 
#la variable se actualiza y en el explorador de variable va a quedcar la ultima variable 

a = "hola mundo"
print(a)

#%%

#CONONOCER EL TIPO DE DATO  UTILIZAMOS TYPE
#-----------------------------------------------

#Te va arrojas <class< 'int' lo cual significa que es un entero 
print(type(3))

#PUDES HACER LO MISMO CON CUALQUIER OTRA VARIABLE 

print(type(True), )
print(type(2 + 3j))
#%%
#ESTRUCTURA DE DATOS: TUPLA, LISTA,  CONJUNTO, DICCIONARIO
#----------------------------------------------------------------


#TUPLA  es como una const 
#----------------------------------
#Es como definir un Array en C, pero con datos de diferentes tipos si los deseas
#OJO: EN LA TUPLA PUEDEN IR DATOS DE DIFERENTES TIPOS 
# solo que aca no podes modificar el valor de cada poosicion en la lista !

#EStamos definiendo una tupla 
t = (1, True, 3.5)
print(type((1, 2, 3, True)))
print(t[1]) # te imprime el true 
#no pudes hacer !
# t[0] = 100  ESTO NO ES VALIDO 

#%%
#LISTA - esto es con []
#------------------------------------
#UNA LISTA ES COMO UNA TUPLA PERO ACA SI PUEDO MODIFICAR LOS DATOS
l = [1, 2, "hola", True, 4.6, 1 + 3j]
#Si imprimimos la lista la imprime tal cual como esta
print(l)

#imprimir un caracter
print(l[2])
l[2] = 5
print(l[2])

#imprimir con indices negativos
#Vamos imprimir el ultimo en la lista
print(l[-1]) 

#Imprimir en un rango definido
#desde el indice 2 hasta el 5
print(l[2:5])

#Si quieres imprimir de 2 en 2
print(l[::2])
#%%

#CONJUNTO  esto es con {}
#---------------------------------
#ES COMO LOS ANTERIORES SOLO QUE EN ESTE NO HAY UN ORDEN A SEGUIR 
#OSEA NO TIENE ORDE L[0] O COSAS ASI, Ademas no permite duplicados

conjunto = {1, 2, True, False, 1 +32j}
#puedes hacer operaciones como union, intersecpion de conjuntos etc


#%%
#DICCIONARIO
#--------------------------------------------
#Funciona como un indice personalizado 
#el valor que almacena puede ser cualqauier cosa, int, string, listas, otros diccionarios,,etc

meses = {1:"enero", 2: "febrero", 3:"Marzo"}
print(meses[1])  
#%%
#OPERACIONES LOGICAS Y DE RELACION 
#--------------------------------------------------------------
print("10 > 3:", 10 > 3)
print("5 <= 5:", 5 <= 5)
print("12 != 10:", 12 != 10)           # El operador "!" es la negación de una operación
print("12 > 33/3:", 12 > 33/3)         # Las operaciones de relación tienen menor precedencia que las aritméticas
print("'a' < 'b':", 'a' < 'b')         # La minusculas estan en orden alafabético?
print("'A' < 'a'", 'A' < 'a')          # La secuencia de letras considera las mayúsulas primero?
print("12 < 15 < 20:", 12 < 15 < 20)   # el valor 15 esta entre 12 y 20?
print("20 > 15 > 10", 20 > 15 > 10)    # el valor 10 esta entre 20 y 10?

#TAMBIEN ESTAN LOS STANDR QUE SON AND Y OR

#%%
#ASIGNACION DE VARIABLE CON INPUT
#--------------------------------------------------------
#lo que insertamos automaticamente es un string, pero puedes ingrear nuymeros o lo que sea 

edad = input("Ingrese su edad: ")
print("hola, tu edad es",edad,"años")

#Pero que pasa si quiero hacer un calculo con el valor ingresasdo 

result = 3 * edad
print("Tu edad multiplicada por 3 es", result)
#OBSERVA QUE TE SALE 777 si un caso ingresas a edad el valor de 7

#LO QUE VAS HACER ES  COLOCAR ANTES DE ESO EL TIPO DE VARIABLE QUE QUIERS
#CONVERTIR UN DATO DE UN TIPO A OTRO 

result = int(edad) * 3
print("Tu edad multiplicado por 3 es: ", result)


#%%

nombre = input("Ingresa tu nombre: ")
print("Hola", nombre + "!") 

#%%
#TODO F-STRING
#FORMATO DE VISUALIZACION NUMERICA
#-------------------------------------------------------------------------------
#FORMAT 
#-------
#en las llaves van a ir los valores que coloquemos en el format en respectivo orden

print("{} + {} = {}".format(10, 20, 10 + 20))

#OJO: ADENTRO DEL PARENTESIS SI DESEAMOIS PODEMOS DEFINIR EL FORMATO DE VISUALIZACION DEL CARACTER !

peso = 82
altura = 1.72
imc =  (peso / altura) ** 2
#en el corchete al poner  :.2f estamos diciendo que el format va a salir con 2 decimales 
print("{} / {:.2f} ^ 2 = {:.2f}".format(peso, altura, imc))


#EJEMPLO 2
#podemos escoger el orden en que se imprimen
nombre1 = "KIRIO PRAGH"
nombre2 = "MARIO TONITELI"
print("WELCOME, {1} y {0}".format(nombre1, nombre2))

#%%
#TAMAÑO DE IMPRESION ( f string)

#con formato tambien podemos espeficiar el tamaño del 
#espacio de impresion de una cadena 

#va imprimir el formato pero en un espacio de 40 cartacteres y alineado a la dercha 
print("{:>40}".format("fecha: 28/02/2025"))
print() # es una linea vacia

# :^40 significa que lo va a centrar en un espacio de 40 caracteres 
print("{:^40}".format("Alumnos matriculados"))
print("{:^40}".format("===================="))

#nos dice que el formato se imprime alineado a la iezquiera en un espacio de 30 pero el resto lo llena con puntos 
print("{:.<30} {}".format("Aremando Paredes", "u439873848"))

#lo mismo que el anterior pero lo rellena con -
print("{:-<30} {}".format("Aremando Paredes", "u439873848"))

#%%
#UN USSO MAS OPTIMO PARA F STRING

nombre = "Elvio"
peso = 82
altura = 1.84
imc = 4355454.45435
print(f"Paciente:  {nombre}")
print("=" * 15)
print(f"IMC : {peso} / {altura:.2f} ^ 2 = {imc:.2f}")

#%%
#SPLIT

#lo que haces es dividir la cadena en secciones, osea en palabras

nombre, apellido = input("INGRESE SU NOMBRE Y APELLIDO: ").split()
print("WELCOME",apellido,",",nombre) 
#%%