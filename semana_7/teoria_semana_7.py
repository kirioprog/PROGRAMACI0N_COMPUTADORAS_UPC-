#todo GESTIONAR LAS RUTAS EN PYTHON

import os 

#TODO CON OS HABLAMOS CON EL SISTEMA OPERATIVO 


# construimos la ruta(string) en donde esta este archivo teoria_semana_7.py

#os.path.join( ) une los diferentes componentes de la ruta 
#os.sep pone el separador en automatico para que no lo hagas manual 
ubicacion = os.path.join("C:", os.sep,"Programacion_de_computadoras", "semana_7", "teoria_semana_7.py")
print(ubicacion)
#observas que es un string
print(type(ubicacion))
#%%
#TODO SABER EN QUE DIRECTORIO ESTAMOS TRABAJANDO 

#os.getcwd()pregunta cual es el directorio de trabajo actual 
info = os.getcwd()
print("el directorio de trabajo es ", info)
#%%
#todo MOVERNOS EN EL DIRECTORIO 
print("ubicacion actual es ",info)
#recuedas que cd .. retrocidia en el directorio eso es lo que hace os.chdir("..")
os.chdir("..")
info_new = os.getcwd()
print("la nueva ubicacion de directorio es", info_new)
#%%
os.chdir("semana_7")
#%%
#TODO CREAR DIRECTORIO 
#creo un nuevo directorio(carpeta)
os.mkdir("new_dir")

# me muevo al directorio new_dir
os.chdir("new_dir")
print(os.getcwd())
#%%
#todo ELIMINAR DIRECTORIO 
os.chdir("..")
#ELIMINO EL DIRECTORIO new_dir para esto debemos estar ubicacion padre  de new_dir( por eso lo de arriba)
os.rmdir("new_dir")
print(os.getcwd())
#%%
#todo HACER UN LISTADO DE DIRECTORIO 
#vamos a ver todos los archivos que hay en el directorio en el que estamos ubicados 

print(os.listdir())

#%%
#todo ARCHIVOS TXT

#todo MODOS DE LECTURA Y DEMAS 
#LEER UN ARCHIVO EXISTENTE
mode = 'r'
#ESCRIBIR EN UN ARCHIVO EXISTENTE O SINO EXISTE LO CREA
mode = 'w'

#Agregar un archivo
mode= 'a'

#todo INTEPREATACION DE CARACTERES

inte1 = 'utf-8'

inte2 = 'latin-1'
#%%
meses: list[str] = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'set', 'oct', 'nov', 'dic']

# Se abre el archivo de texto en modo escritura (si no existe se crea un archivo nuevo)

#PARA ABRIR EL ARCHIVO UTILIZAN OPEN(nombre de archivo, mode, intepretacion)
file = open("meses.txt", mode='w', encoding='utf-8')

# escribimos dentro del archivo con file.write
for idx, etiqueta in enumerate(meses):
    file.write(f"{idx+1:2} {etiqueta} \n")

# Se cierra el archivo
#guardamos y cerramos el archivo 
file.close()  

#%%
#vamos a revisar elc odigo anterior con el #todo MODO R

file = open("meses.txt", mode='r', encoding='utf-8')
#RETORNA TODO EL CONTENIDO DEL ARCHIVO 
texto = file.read()
#GUARDAMOS Y CERRAMOS 
file.close()

print(texto)

#%%
#todo CONTEXT MANAGER 
#CREAR EL ARCHIVO Y AÑADIRLE CONTENIDO 

# Creamos el cursor con un bloque with y cuando este termine el archivo se cerrara
meses: list[str] = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'set', 'oct', 'nov', 'dic']

with open("meses2.txt", mode='w', encoding='utf-8') as file:
    for idx, etiqueta in enumerate(meses):
        file.write(f"{idx+1:2} {etiqueta}\n")     # \n: Salto de linea
 #%%       
# No utilizaremos el modo ya que por defecto es 'r' (lectura)

#WITH es como un asistente automatico para manejar archivos 

#voy a ingrear al archivo meses2.txt pero toodo lo que este adentro de with llamaremos a meses2.txt como file 

with open("meses2.txt", encoding='utf-8') as file:
    #leemos todo lo que esta en el archivo 
    texto = file.read()

print(texto)

#%%
#todo ARCHIVOS COMO ITERABLES 
#RETONRAR EL STR AL QUE ESTA APUNTADO EL CURSO HATA \n 
readline()

#Retorna una lista con  las lineas del archivo, incluyendo \n al final de cada elemento
readlines()
#%%
# Utilizemos los parametros por defecto: lectura, encoding estandar
with open("meses.txt", encoding='utf-8') as file:
    #recuerda que estrip recorta los espacios en blanco, tabulaciones y saltos de linea 
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())
#%%
with open("meses.txt", encoding='utf-8' ) as file:
    print(file.readlines())
#%%
with open("meses.txt", encoding = 'utf-8') as file:

#el for va a leeer linea por linea 
    for line in file:

        print(line.strip()) 
        
#%%
#todo CREACION DE ARCHIVO NUMEROS.TXT
with open("numeros.txt", mode='w') as file:
    for num in range(1, 11):
        file.write(f"5 {num}\n")
        
#Mostremos su informacion 
with open("numeros.txt") as file:
    text: str = file.read()

print(text)

#%%
#todo HACER OPERACION MATEMATICA CON UN ARCHIVO TXT
with open("numeros.txt") as file:
    for line in file:
        #desempaquetamos cada fila  pero quitaqndo los saltos de linea el split para para separarlas en una lista 
        num1, num2 = line.strip().split()
        print(f"{num1} x {num2} = {int(num1) * int(num2)}")
        
#%%
#todo GUARDAR DATOS EN EL ARCHIVO 
# mode 'a' anexa nuevas lineas sobre un archivo
with open("numeros.txt", mode='a') as file:
    for mult in range(11, 21):
        # El valor entero generado por range se convierte en parte de un str
        file.write(f"5 {mult}\n")   
        
with open("numeros.txt", mode='r', encoding='utf-8') as file:
    texto_completo = file.read()
    print(texto_completo)
    
#%%
#%%
#todo ARCHIVOS CSV 

#CSV significa "Valores Separados por Comas"
#Es un archivo de texto plano para guardar datos como en Excel.
#No se debe leer con .split() porque un valor puede tener comas (ej: "1,200.50")
#Para eso usamos la librería especial 'csv'
import csv

#%%
#todo ESCRIBIR UN ARCHIVO CSV
import csv

#primero preparamos los datos
empleados: list[list[str,str]] = [
    ["2/3/2024 07:20", "Elvio Lado"],
    ["2/3/2024 07:22", "Elmer Curio"],
    ["2/3/2024 07:30", "Elba Lazo"],
    ["2/3/2024 07:36", "Susana Oria"],
    ["2/3/2024 07:49", "Armando Paredes"]
]

filename: str = "entrada.csv"

#abrimos el archivo
#mode='w' es para escribir (crea el archivo si no existe)
#newline='' es para evitar lineas en blanco dobles en Windows
with open(filename, mode='w', newline='') as csv_file:
    
    #csv.writer() crea un objeto escritor sobre el archivo
    #delimiter=';' establece el separador (compatible con Excel)
    writer = csv.writer(csv_file, delimiter=';')
    
    #writer.writerow() escribe una lista como una fila
    #escribimos la primera fila (el encabezado)
    writer.writerow(["HORA", "EMPLEADO"])
    
    #recorremos los registros para escribirlos
    for registro in empleados:
        #escribimos cada registro en una fila
        writer.writerow(registro)

print(f"Archivo generado: {filename}")
#%%

#todo LEER UN ARCHIVO CSV (CON CSV.READER)
import csv

#abrimos el archivo
#no se pone mode='r' porque es el modo por defecto
with open("entrada.csv") as file:
    
    #csv.reader() crea un objeto lector para iterar sobre las lineas
    #delimiter=';' le dice cual es el separador que debe buscar
    reader = csv.reader(file, delimiter=';')
    
    #next(reader) # con esto pasamos a la siguiente linea: eliminamos el encabezado
    next(reader) 
    
    #recorremos el lector, 'line' es una lista
    for line in reader:
        #line[0] es el primer elemento ('HORA')
        #line[1] es el segundo elemento ('EMPLEADO')
        print(f"* Nombre: {line[1]:20} Hora de ingreso: {line[0]}")

#%%
#todo LEER UN ARCHIVO CSV (CON CSV.DICTREADER)
import csv

filename: str = "entrada.csv"

#abrimos el archivo
with open(filename, encoding='utf-8') as file:
    
    #csv.DictReader() crea un lector que convierte cada fila en un diccionario
    #usa la primera fila (encabezado) como las llaves (keys)
    reader = csv.DictReader(file, delimiter=';')
    
    #NO SE NECESITA next(reader), DictReader maneja el encabezado solo
    
    #recorremos el lector, 'line' es un diccionario
    for line in reader:
        #accedemos a los datos por el nombre de la columna (la llave)
        #line['HORA']
        #line['EMPLEADO']
        print(f"* Nombre: {line['EMPLEADO']:20} Hora de ingreso: {line['HORA']}")