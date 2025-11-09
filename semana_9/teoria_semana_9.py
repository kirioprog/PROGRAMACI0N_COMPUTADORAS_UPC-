# -*- coding: utf-8 -*-
# OOP - PARTE 1 
# en un objeto juntas datos (atributos) y funciones (métodos) que operan sobre esos datos
# eso es OOP, programación orientada a objetos

#%%
# TODO: QUE ES OOP
# OOP = Programación Orientada a Objetos
# es un paradigma (forma de pensar) donde integras datos y funciones en una sola unidad: el objeto
# por ejemplo: un objeto lápiz tiene propiedades (color, punta, peso) y acciones (mover, subir, bajar)

#%%
# TODO: isinstance para verificar tipos
t = 'hola'
isinstance(t, str)   # True -> t es un objeto clase str
# esto te sirve para validar que alguien te pasó el tipo correcto, nada más

#%%
# TODO: OBJETO - definición práctica
# ¿Cómo definiría un "objeto"? En programación:
# - Un objeto es algo que tiene un conjunto de propiedades (atributos)
# - Un objeto es algo que puede realizar distintas acciones (métodos)

# por ejemplo un lápiz:
# propiedades: color, tipo, punta, peso, longitud, posición x, posición y
# acciones: mover en plano, subir, bajar

#%%
# TODO: CLASE - definición
# una clase es un prototipo que define TODOS los atributos y acciones de un objeto
# es la plantilla (receta) para crear (instanciar) un objeto

# por ejemplo: clase Car define atributos (marca, modelo, motor, ruedas, color)
# y acciones (acelerar, frenar, girar)
# los objetos Audi, Nissan, Volvo son INSTANCIAS de la clase Car

# terminología:
# - Propiedades se denominan ATRIBUTOS
# - Acciones se denominan MÉTODOS

#%%
# TODO: QUE ES OOP Y POR QUE EXISTE
# OOP = Programación Orientada a Objetos
# la idea es que NO andes metiendo datos sueltos y funciones sueltas por ahí
# en cambio, creas una clase (receta) que define cómo se ve un objeto y qué puede hacer

#Por ejemplo cuando se escribe el siguiente código:
t = 'hola'
#Se esta "instanciando" un "objeto" t clase str. Esto se puede verificar con la instrucción isinstance:
    
# TODO: isinstance para verificar si algo es de cierto tipo
isinstance(t, str)   # True -> confirma que t es tipo string
# esto te sirve cuando quieres validar que alguien te pasó el tipo correcto

#%%
# TODO: HERENCIA Y POLIMORFISMO - conceptos clave
# Herencia: una clase puede derivar de otra y heredar sus atributos y métodos
# ejemplo: Alumno(Persona) hereda todo de Persona y puede añadir cosas propias

# Polimorfismo: el mismo método hace cosas distintas en clases hijas
# ejemplo: Auto.acelerar() hace una cosa, Bicicleta.acelerar() hace otra distinta

#%%
# TODO: AGENDA DE CONTACTOS - FORMA PROCEDIMENTAL (lista de diccionarios)
# primero lo hacemos sin usar objetos, con lista de diccionarios
# esto es lo que vamos a mejorar luego con OOP

contactos = [
    {
        'nombre': 'Dina Mita',
        'telefono': '927-234-113',
        'email': 'dmita@mail.com'
    },
    {
        'nombre': 'Elvio Lado',
        'telefono': '997-332-253',
        'email': 'elado@mail.com'
    },
    {
        'nombre': 'Elmer Curio',
        'telefono': '927-234-113',
        'email': 'ecurio@mail.com'
    },
    {
        'nombre': 'Alan Brito',
        'telefono': '345-1921',
        'email': 'alan.brito@business.com'
    }
]

# TODO: ACCEDER A LOS DATOS
# la lista contactos contiene diccionarios, cada uno es un contacto
print(contactos[0])    # Primer contacto de la lista de contactos

# para acceder a un valor específico usas la llave
print(contactos[0]['nombre'])    # Nombre del primer contacto de la lista
print(contactos[0]['telefono'])  # Teléfono del primer contacto de la lista
print(contactos[0]['email'])     # Email del primer contacto de la lista

 #%%
# TODO: FUNCIONES PARA LA AGENDA PROCEDIMENTAL

def agregar_contacto(contactos):
    # esta función pide datos al usuario y y crea un dicionario que agrega sobre una lista de contactos (argumento de entrada) 
    print("\nIngreso de contactos")
    print("------------------------")
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese telefono: ")
    email = input("Ingrese email: ")
    #todo añadir un contactor a una lista diccionario 
    contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})
    return None

def listar_contactos(contactos):
    # esta función barre los elementos de la lista e imprime de forma enumerada los contactos
    print("\nInformacion de contactos")
    print("------------------------")
    for idx, contacto in enumerate(contactos, start=1):
        print(f"\nCONTACTO {idx}:")
        print(f"   Nombre: {contacto['nombre']}")
        print(f"   Telefono: {contacto['telefono']}")
        print(f"   Email: {contacto['email']}")

# # ejemplo de app con menú 
while True:
     print("\nAgenda de contactos")
     print("-----------------")
     print("[1] Agregar contacto")
     print("[2] Listar contactos")
     print("[0] Salir")
     opc = input("> : ")
     if opc == '0':
         break
     elif opc == '1':
         agregar_contacto(contactos)
     elif opc == '2':
         listar_contactos(contactos)
     else:
         print("Opcion invalida")

#%%
# TODO: CLASE Y OBJETO - ejemplo básico
# clase = plantilla. objeto = instancia.
#no entiendo para que sirve 

class Persona:
    pass   # pass significa "aún no hay contenido, pero la clase existe"

persona1 = Persona()
persona2 = Persona()

print(persona1)
print(persona2)
# verás dos direcciones diferentes en memoria: <__main__.Persona object at 0x...>
# cada instancia (objeto) ocupa su propio espacio en memoria( persona )

#%%
#todo
# TODO: CONSTRUCTOR - __init__ y SELF
# cuando haces Persona() se ejecuta automáticamente EL METODO  __init__


# self es una etiqueta que sea reemplazad por el objeto futuro 
# self._nombre es el atributo "nombre" de lo que luego sera persona1

class Persona:
    # self es el objerto que se esta creando a partir de la clase persona 
    def __init__(self):
#creamos sun atributo(propiedad)) llamada nombre que pertenecera al objeto self y le damos el valor inicial de NN
        self._nombre = 'NN'

#%%
# TODO: REPRESENTACIÓN - __repr__    __str__para mostrar el objeto

class Persona:
    def __init__(self):
        self._nombre = 'NN'
        
    def __str__(self):
        # se llama automaticamente cuando utilizas print 
        return "Objeto Persona - Print"

    def __repr__(self):
        #se llama automaticamente cuando escribes el nombre del objeto en la terminal 
        return "Objeto Persona - Representacion"

persona1 = Persona()
print(persona1)

#ahora ingresa persona1 en la terminal y se invocara a persona 1 eso es lo que hace repr 
#%%
#todo REDEFINIMOS LA CLASE  para que ambas acciones repr y init retornen lo mismo 
class Persona:
    def __init__(self):
        self._nombre = 'NN'
    
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    
persona1 = Persona()
print(persona1)

#ingresamos persona1 en la terminal y te retornara lo mismo 

#%%
# TODO: SETTER - nos peremite asignar un valor a un atributo de la clase 
class Persona:
    #inicializamos el atributo con un vacio ''
    def __init__(self):
        self._nombre = ''
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    
#camb iar el valor del atributo protegido ( _nombre)
# todo definimos un metodo que acepta 2 argumentos
#val es el nuevo valor que quieres asignar a nombre 

    def set_nombre(self, val):
        #val contiene el nuevo valor que quieres asignar a nombre 
        self._nombre = val 



persona1 = Persona()
#tomar el valor de val y asignarle al atributo interno self._nombre 
persona1.set_nombre('Dennis')
print(persona1)
#%%
#el set_persona solo deberia aceptar valores de clase str entonces agregemosle esa restriccion 
class Persona:
    def __init__(self):
        self._nombre = ''
    
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    
    def set_nombre(self, val):
        #verificamos que val sea str y que el primer valor no sea un espacio en blanco
        if isinstance(val, str) and val[0] != ' ':
            self._nombre = val
        else:
            #levantamos un error con raise Typerror 
            raise TypeError("El atributo 'nombre' debe de ser un objeto 'str'")
            
persona1 = Persona()
persona1.set_nombre(1234)
print(persona1)
            
            
#%%
# TODO: GETTER - método para LEER datos
# el getter nos permite acceder a los valroes de una propiedad, osea de los atributos en especificos 


class Persona:
    def __init__(self):
        self._nombre = ''
    
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    
    def set_nombre(self, val):
        if isinstance(val, str):
            self._nombre = val
        else:
            raise TypeError("El atributo 'nombre' debe de ser un objeto 'str'")

#TODO Acceder al valor del atribujo _nombre desde la terminal  
    def get_nombre(self):
        #Accedemos al atribujo interno y devuelve su valor actural 
        return self._nombre
    
    
# ejemplo rápido
persona1 = Persona()
persona1.set_nombre("Alan")
persona1.get_nombre()
print(persona1)

#%%
# DEFINA COMPLETAMENTE LA CLASE PERSONA CON TODOS LOS ATRIBUTOS NECESARIOS
# Y LOS SETTERS Y GETTERS CORRESPONDIENTES
class Persona:
    def __init__(self):
        self._nombre = ''
        self._telefono = ''
        self._email = ''
    
    def __repr__(self):
        return "Persona:[nombre:'{}', telefono:{}, email:{}]".format(
            self._nombre, self._telefono, self._email)
    
    def set_nombre(self, val):
        #all devuelve true si todos los elementos de la lista son verdaderos 
        # Validamos que el nombre contenga caracteres y espacios en blanco
        if isinstance(val, str) and all([chars.isalpha() for chars in val.split()]):
            self._nombre = val
        else:
            raise TypeError("El atributo 'nombre' debe de ser un objeto 'str'")
            
    def get_nombre(self):
        return self._nombre
    
    def set_telefono(self, val):
        if isinstance(val, str):
            self._telefono = val
        else:
            raise TypeError("El atributo 'telefono' debe de ser un objeto 'str'")
            
    def get_telefono(self):
        return self._telefono
    
    def set_email(self, val):
        if isinstance(val, str):
            self._email = val
        else:
            raise TypeError("El atributo 'email' debe de ser un objeto 'str'")
            
    def get_email(self):
        return self._email

#%%
# INSTANCIAMIENTO DE UN OBJETO CLASE PERSONA Y PRUEBA DEL OBJETO
p1 = Persona()
p1.set_nombre("Alan")
p1.set_telefono("987-282-821")
p1.set_email("alan@mail.com")

p1.get_nombre()
p1.get_telefono()
p1.get_email()

print(p1)
#%%
#verifiquemos excepciones 

# ESTA CELDA DEBERIA DE GENRAR UNA EXCEPCION
p1 = Persona()
p1.set_telefono(987112123)
#%%
# ESTA CELDA DEBERIA GENERAR UNA EXCEPCION
p1 = Persona()
p1.set_email(12345)
#%%
def ingresar_contacto():
    contacto = Persona()
    contacto.set_nombre(input("Ingrese nombre: "))
    contacto.set_telefono(input("Ingrese telefono: "))
    contacto.set_email(input("Ingrese email: "))
    
    return contacto

def ingresar_contacto():
    contacto = Persona()
    contacto.set_nombre(input("Ingrese nombre: "))
    contacto.set_telefono(input("Ingrese telefono: "))
    contacto.set_email(input("Ingrese email: "))
    
    return contacto

def buscar_contacto(contactos):
    # El argumento "contactos" es una lista de Personas: [Persona(), Persona(), ...]
    found = False
    nombre = input("Ingrese el nombre del contacto: ")
    
    for contacto in contactos:
        if nombre.upper() in contacto.get_nombre().upper():
            print(contacto)
            found = True
            
    if not found:
        print("No hay un contacto con ese nombre en la agenda")
        

def listar_contactos(contactos):
    # El argumento "contactos" es una lista de Personas: [Persona(), Persona(), ...]
    if len(contactos) == 0:
        print("No hay contactos que listar")
    else:
        print(f"Contactos en la lista: {len(contactos)}")
        print()
        for idx, contacto in enumerate(contactos):
            print("   {}: {}".format(idx+1, contacto))
            


# Cargamos un contacto base en la lista de contactos
p = Persona()
p.set_nombre("Alan")
p.set_telefono("987-282-821")
p.set_email("alan@mail.com")
contactos = [p]

while True:
    print("\nAgenda de contactos")
    print("-----------------")
    print("[1] Nuevo contacto")
    print("[2] Buscar contactos")
    print("[3] Mostrar todos")
    print("[0] Salir")
    opc = input("> ")
    
    if opc == '1':
        try:
            contactos.append(ingresar_contacto())
        except (ValueError, TypeError):
            print("Ingreso inválido")
    elif opc == '2':
        buscar_contacto(contactos)
    elif opc == '3':
        listar_contactos(contactos)
    elif opc == '0':
        break
    else:
        print("Opcion invalida")