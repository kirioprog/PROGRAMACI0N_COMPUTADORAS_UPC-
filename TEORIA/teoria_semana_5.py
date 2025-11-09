# -*- coding: utf-8 -*

#%%
#todo STRING 
print("soy un string")
print(type(""))

#en este caso estas poniendo triple comilla para que la linea que esta debadjo se imprima en una linea abajo 
print("""Esto se imprimira en una linea
y esto en la segunda linea""")

print()
print("Esto se imprime en una linea \n y esto en otra ")

#%%
texto : str = "Soy un texto de prueba"

print(texto[0])
#REcuerdas que poner -1 significa que parte desde el ultimo 
print(texto[-1])
#imprime los 10 primero caracteres 
print(texto[:10])
#El formato es [inicio:fin:paso]
#en este caso te esta imprimiendo la posicion 0,3,6,9,12,15,18,21
print(texto[::3])
print(texto[::-1])
#%%
#TODO LOS STRING SON INMUTABLES OSEA NO PUEDES CAMBIAR SUS CARACTERES INDIVIDUALES 
texto1 : str = "hola"
texto1[0] = "m"
#%%
#TODO UTILIZAR FOR CON LOS STRING 
for char in 'string':
    print(char)
#te imprime cara caracter del string 
print()
for can in "este es un ejemplo":
    print(can)

#%%
#TODO OPERACIONES CON STRING 
#vamos a imprimir 3 zetas y seguido de esto 6 puntos 
print("z" * 3 + "." * 6)

titulo = "mensaje a trabajar"
print(titulo)
#como ya imprimimos el mensaje titulo y quiero ponerlo bonito voy a poner = pero la cantidad de veces  sera  ighual a la longitud del mensaje 
print("=" * len(titulo))
#%%
#TODO CONOCER EL CODIGO UNICODE 
#NO SIRVE MUCHO JEJE 
#te tiene que salir A = 65 porque 65 es el codgio de la letra A en unicode
print("A = ", ord("A"))
print("65 = ", chr(65))

#%%
#TODO IMPORTANTE !!METODOS DE UN STRING 
#podemos observar los usos que le podemos dar al string 
dir(str)

#ELIMINAR CARACTERES
#al eleiminar un caractere obtienes un nuevo string 

texto = "            ESTE ES UN NUEVO TEXTO DE PRUEBA      .             "

print(f"|{texto}|")

#Eliminar los caracteres adicionales( ESPACIO, SALTO DE LINEA, TAB ) l inicio y al final de una cadena 
print(f"{texto.strip()}")

#elimina los caracteres adicionales al inciio de una cadena
print(f"{texto.lstrip()}")

#elimina los caracter adicionales al final de la cadena 
print(f"{texto.rstrip()}")

#%%
#El método .strip(",.grt") quita los caracteres , . g r t pero solo de los extremos (inicio y final), no del medio.
print(",,,,,rrttgg.....banana....rrr".strip(",.grta"))

#%%
#TODO CAMBIAR LOS CARACTERES DE UN STRING
#TODO
#TODO

texto = "m   vamos a probar otra vez    ."
#convierte el primer caracater en mayuscula
print(texto.capitalize())

#convierte todo el texto en mayuscula
print(texto.strip().upper())
#convierte todo el texto en minuscula 
print(texto.strip().lower())

#Convierte el string en un titulo, osea cada primera palabra del texto es mayuscula 
print(texto.strip().title())

#intercambia mayusculaz por minusculas y viceverza
print(texto.strip().title().swapcase())

#%%
#TODO METODOS ASOCIADOS A OCURRENCIAS EN UN STRING O SUBSTRING 
#TODO

texto = "este es un  texto de prueba "
#CONTAR EL NUMEROI DE VECEZ QUE UN SUBSTRING ESTA EN UN STRING
print(texto.count("es"))
#reemplaza un substring por otro , en este caso reemplazo es por no es 
#OJO CON EL ESPACIO REEMPLAZA CON TODO ESO 
print(texto.replace("es ", "no es "))
print(texto)
#NO SON LO MISMO 
print(texto.replace("es", "no es"))

#retorna la ubicacion del substring, en este caso e se encuenta en la posicion 0 por eso te arroja 0
print(texto.find("es"))
#retorna 5 por "es" tal cual se encuentra en la posicion 5
print(texto.rfind("es"))


#%%
#todo STRING Y JOIN

#vamos a separar cadda palabra a travez del espacio, esto nos va a crear una lista
las_palabras = "un alumno upecino".split()
print(las_palabras)

#toma todas las palabras separados por espacio y las une mediante "lo que quieras que valla que una esto, es como una cadena que los ata"
print("-".join(las_palabras))

#%%
#CONSULTAR POR CARACTERES 
print("abcde".isalpha())
print("abc123".isalpha())
print("123".isdigit())
print("dina4ever".isalnum())
print("Hola\ntexto".isprintable())
print("hola".islower())
print("HOLA".isupper())
print("123".isupper())
print("   ".isspace())

#%%
#todo TIME
import time 
#nos retorna la fecha, mes, año, dia , hora , minuto, segundo local
print(time.localtime())

time_now = time.localtime()
#tambien puede ser time_now: time = time.localtime()
#el punto entre time_now y (lo que busco ) esta porque asi puedo acceder a timeÑ_n ow como en las estructuras de datos 
print(f"{time_now.tm_mday:0>2}/{time_now.tm_mon:0>2}/{time_now.tm_year}")

 #%%
#todo GENERAR RETRASOS COMO LO HACIAS EN ARDUINO
#todo
#time.sleep(tiempo en segundo )

print("iniciando en ", end = '')
for num in range (3, 0, -1) :
    print(f"{num}...", end = '')
    #Queremos que espere 1 segundo 
    #osea ejecuta todo lo anterior y espera 1 segundo antes de pasar al siguiente paso 
    time.sleep(1)
else:
    print("0")
    
#%%
#convierte una estructura de tiempo a un string legible 

#obtenemos el tiempo actual 
time_now = time.localtime()
#hora minuto segundo 
time.strftime("%H:%M:%S", time_now)


#convertir un texto a un objeto de tiempo 
info_fecha = "12/4/2025"
time.strptime(info_fecha, "%d/%m/%Y")

#%%

from datetime import datetime 

#OBTENER LA FECHA LOCAL 
datetime.now()
#esto es mas legible 
print(datetime.now())

print(f"Hora actual: {datetime.now():%H:%M:%S}")
print(f"Fecha Actual: {datetime.now():%d/%m/%Y}")


from datetime import timedelta 

time_now = datetime.now()

#si o si tienes que poner days 
time_delta = timedelta(days= 100)

print(f" Fecha en 100 dias : {time_now + time_delta:%d / %m / %Y}")

#%%
#OBTENER LOS DIAS TRANSCURRIDOS TRAS TU FECHA DE NACIMIENTO 
fec_nac = datetime.strptime(input("Ingrese su fecha de nacimento ['DD/MM/YYYY']: "), "%d/%m/%Y")
print("Dias de vida transcurridos:", datetime.now() - fec_nac)

#%%
#CALCULAR FUTURAS SESIONES DE CLASE
fec_ini: datetime = datetime(2025, 3, 20)     # Se define un datetime de forma directa (3 de marzo del 2025)
delta: timedelta = timedelta(weeks=1)

print("Fechas de las sesiones de clase:")

fec: datetime = fec_ini
for idx, _ in enumerate(range(15), start=1):
    print(f"\t* Sesion {idx:>2}: {fec:%d/%m/%Y}")
    fec += delta
