# OOP - PARTE 1 (apunte style tuyo, sin formalismos xd)
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
# TODO: OBJETOS EN PYTHON - todo es una clase
# En Python, todo es un objeto y todo es una clase
# cuando haces t = 'hola' estás instanciando un objeto clase str

t = 'hola'
isinstance(t, str)   # verificas si t es instancia de la clase str

# t no es "formalmente una variable que vale 'hola'"
# t es un OBJETO clase str con una propiedad de valor 'hola'
# y tiene métodos (acciones) como .upper() para convertir a mayúsculas

t.upper()

# los métodos son acciones que hace un objeto
# sintáxis: obj.metodo()
# es decir, el método upper() se aplica al objeto t, no es genérico

# esta integración de atributos y métodos se llama "ENCAPSULAMIENTO"

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
    # esta función pide datos al usuario y agrega un contacto a la lista
    print("\nIngreso de contactos")
    print("------------------------")
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese telefono: ")
    email = input("Ingrese email: ")
    contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})
    return None

def listar_contactos(contactos):
    # esta función barre los elementos de la lista e imprime los contactos
    print("\nInformacion de contactos")
    print("------------------------")
    for idx, contacto in enumerate(contactos, start=1):
        print(f"\nCONTACTO {idx}:")
        print(f"   Nombre: {contacto['nombre']}")
        print(f"   Telefono: {contacto['telefono']}")
        print(f"   Email: {contacto['email']}")

# # ejemplo de app con menú (comentado para no ejecutarse):
# while True:
#     print("\nAgenda de contactos")
#     print("-----------------")
#     print("[1] Agregar contacto")
#     print("[2] Listar contactos")
#     print("[0] Salir")
#     opc = input("> ")
#     if opc == '0':
#         break
#     elif opc == '1':
#         agregar_contacto(contactos)
#     elif opc == '2':
#         listar_contactos(contactos)
#     else:
#         print("Opcion invalida")

#%%
# TODO: CLASE Y OBJETO - ejemplo básico
# clase = plantilla. objeto = instancia.

class Persona:
    pass   # pass significa "aún no hay contenido, pero la clase existe"

persona1 = Persona()
persona2 = Persona()

print(persona1)
print(persona2)
# verás dos direcciones diferentes en memoria: <__main__.Persona object at 0x...>
# cada instancia (objeto) ocupa su propio espacio en memoria

#%%
# TODO: CONSTRUCTOR - __init__ y SELF
# cuando haces Persona() se ejecuta automáticamente el método __init__
# __init__ es el constructor: inicializa los atributos del objeto

# self es "yo" (el objeto que se está creando)
# todo atributo se guarda en self._nombre

class Persona:
    def __init__(self):
        # _nombre con underscore = convención que dice "esto es privado"
        # Python no lo impide realmente, pero ayuda a comunicar intención
        self._nombre = 'NN'

#%%
# TODO: REPRESENTACIÓN - __repr__ para mostrar el objeto
# __repr__ devuelve un string que representa al objeto
# cuando haces print(objeto) Python usa __repr__ para mostrar qué es

class Persona:
    def __init__(self):
        self._nombre = 'NN'
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)

p = Persona()
print(p)   # verás: Persona:[nombre:'NN']

#%%
# TODO: SETTER - método para GUARDAR datos CON VALIDACIÓN
# el setter valida el dato ANTES de guardarlo
# por qué: si aceptas cualquier cosa sin revisar, después tu código explota

class Persona:
    def __init__(self):
        self._nombre = ''
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    def set_nombre(self, val):
        # validación: que sea string y que cada palabra tenga solo letras
        if isinstance(val, str) and all([part.isalpha() for part in val.split()]):
            self._nombre = val
        else:
            # si no cumple, levanto un error para que se note
            raise TypeError("El atributo 'nombre' debe de ser un objeto 'str'")

#%%
# TODO: GETTER - método para LEER datos
# el getter devuelve el valor del atributo privado

class Persona:
    def __init__(self):
        self._nombre = ''
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    def set_nombre(self, val):
        if isinstance(val, str) and all([part.isalpha() for part in val.split()]):
            self._nombre = val
        else:
            raise TypeError("El atributo 'nombre' debe de ser un objeto 'str'")
    def get_nombre(self):
        return self._nombre

# ejemplo rápido
persona = Persona()
persona.set_nombre('Alan')
print(persona.get_nombre())
print(persona)

#%%
# TODO: CLASE PERSONA COMPLETA - nombre, teléfono, email
# esto es lo que hizo el profe: cada atributo tiene su setter y getter

class Persona:
    def __init__(self):
        self._nombre = ''
        self._telefono = ''
        self._email = ''
    def __repr__(self):
        return "Persona:[nombre:'{}', telefono:{}, email:{}]".format(self._nombre, self._telefono, self._email)
    def set_nombre(self, val):
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

# prueba rápida
if __name__ == '__main__':
    p1 = Persona()
    p1.set_nombre('Alan')
    p1.set_telefono('987-282-821')
    p1.set_email('alan@mail.com')
    print(p1)

#%%
# TODO: PROBAR SETTERS CON VALORES INCORRECTOS
# si descomentas esto, verás el error:
# p1 = Persona()
# p1.set_telefono(987112123)   # TypeError porque es int, no string
# p1.set_email(12345)          # TypeError porque es int, no string

#%%
# TODO: AGENDA DE CONTACTOS - FORMA OOP (usando objetos Persona)
# ahora guardamos objetos Persona en la lista en lugar de diccionarios
# ventaja: validación automática y métodos del objeto

def ingresar_contacto():
    # función que pide datos y devuelve un objeto Persona
    contacto = Persona()
    contacto.set_nombre(input("Ingrese nombre: "))
    contacto.set_telefono(input("Ingrese telefono: "))
    contacto.set_email(input("Ingrese email: "))
    return contacto

def buscar_contacto(contactos):
    # buscamos un contacto por nombre (case-insensitive)
    found = False
    nombre = input("Ingrese el nombre del contacto: ")
    for contacto in contactos:
        # contacto es un objeto Persona, usamos get_nombre() para acceder
        if nombre.upper() in contacto.get_nombre().upper():
            print(contacto)
            found = True
    if not found:
        print("No hay un contacto con ese nombre en la agenda")

def listar_contactos_oop(contactos):
    # listamos todos los contactos (objetos Persona)
    if len(contactos) == 0:
        print("No hay contactos que listar")
    else:
        print(f"Contactos en la lista: {len(contactos)}")
        print()
        for idx, contacto in enumerate(contactos):
            # print(contacto) usa __repr__ del objeto Persona
            print(f"   {idx+1}: {contacto}")

# # ejemplo de app con menú (comentado):
# p = Persona()
# p.set_nombre("Alan")
# p.set_telefono("987-282-821")
# p.set_email("alan@mail.com")
# contactos_oop = [p]
#
# while True:
#     print("\nAgenda de contactos")
#     print("-----------------")
#     print("[1] Nuevo contacto")
#     print("[2] Buscar contactos")
#     print("[3] Mostrar todos")
#     print("[0] Salir")
#     opc = input("> ")
#     if opc == '1':
#         try:
#             contactos_oop.append(ingresar_contacto())
#         except (ValueError, TypeError):
#             print("Ingreso inválido")
#     elif opc == '2':
#         buscar_contacto(contactos_oop)
#     elif opc == '3':
#         listar_contactos_oop(contactos_oop)
#     elif opc == '0':
#         break
#     else:
#         print("Opcion invalida")

#%%
# TODO: CONCEPTOS CLAVE - RESUMEN
# Objeto = instancia de una clase (la "cosa" que hiciste)
# Clase = la receta que define cómo se ve y qué puede hacer el objeto
# Atributo = propiedad del objeto (nombre, teléfono, etc.)
# Método = función que pertenece al objeto (set_nombre, get_nombre, etc.)
# Encapsulamiento = guardar datos privados (_nombre) y accederlos via getters/setters
# __init__ = constructor, se ejecuta cuando haces Persona()
# __repr__ = representación del objeto, lo que ves cuando haces print(obj)
# Herencia = una clase puede derivar de otra (Alumno heredaría de Persona)
# Polimorfismo = el mismo método hace cosas distintas en clases hijas

#%%
# TODO: EJERCICIOS / ACTIVIDADES
# - Implementar completamente la clase Persona con validaciones (arriba está hecho)
# - Probar setters con valores inválidos para ver las excepciones
# - Hacer la app de agenda que permite crear, buscar y listar contactos (procedimental y OOP)

#%%
# TODO: RECOMENDACIONES / CONSEJITOS
# - intenta crear subclases: Alumno(Persona), Empleado(Persona) para practicar herencia
# - crea más métodos en Persona (ejemplo: un método que devuelva todos los datos juntos)
# - luego aprenderás @property que es más limpio que setters/getters clásicos
# - practica mucho: entiende por qué validamos, por qué usamos métodos privados, etc.

#%%
# FIN - Apunte Semana 9 (OOP Parte 1) explicado sin formalismos xd
