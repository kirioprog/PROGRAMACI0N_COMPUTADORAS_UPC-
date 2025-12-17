# -*- coding: utf-8 -*-
# ¡Apuntes de OOP - PARTE 1! (Estilo pa' entender de verdad, sin tanto rollo xd)
# La idea es simple: ¡juntar las cosas! En un objeto metes:
# 1. Los datos (atributos).
# 2. Las funciones (métodos) que usan esos datos.
# Eso es OOP: Programación Orientada a Objetos.

#%%
# TODO: QUE ES OOP - Definición simple
# OOP = Programación Orientada a Objetos.
# Es solo una forma de pensar/organizar el código (un "paradigma").
# ¿Qué hace? Coge los datos y las funciones que los usan y los mete en una "caja" (el objeto).
# Ejemplo: Un LÁPIZ (el objeto) tiene Propiedades/Datos (color, peso) y Acciones/Funciones (dibujar, borrar).

#%%
# TODO: isinstance - ¡El detector de tipos!
t = 'hola'
isinstance(t, str)    # Esto pregunta: ¿t es un objeto de la clase 'str' (string)? True.
# USOS: Lo usamos muchísimo en los SETTERS (más abajo) para asegurarnos de que el usuario
# no intente meternos un número donde esperamos un nombre, por ejemplo. ¡Para validar!

#%%
# TODO: OBJETO - La unidad de trabajo
# Un "objeto" es nuestra "caja" concreta. Piensa en él como:
# 1. Un grupo de datos que le pertenecen (ATRIBUTOS).
# 2. Un grupo de cosas que sabe hacer (MÉTODOS/Acciones).
# Ejemplo:
# Objeto LÁPIZ:
# - ATRIBUTOS: color='rojo', punta='fina', peso=10gr
# - MÉTODOS: dibujar(linea), afilar()

#%%
# TODO: CLASE - El molde (La Receta)
# Una CLASE es el *molde* o la *receta* que usamos.
# Define la ESTRUCTURA: dice qué atributos va a tener y qué métodos va a saber hacer.
# Cuando ejecutas `mi_objeto = Clase()`, estás creando una INSTANCIA (la galleta).

# Ejemplo con tu idea del Vehículo:
# CLASE Vehiculo (El Molde Grande) -> Define: velocidad, color, peso, método acelerar().
#                                     Sirve para crear clases hijas como VehiculoRuedas o Velero.
# TERMINOLOGÍA CLAVE:
# - Propiedades/Datos = ATRIBUTOS
# - Acciones/Funciones = MÉTODOS

#%%
# TODO: HERENCIA Y POLIMORFISMO - Conceptos Pro (¡Con el ejemplo del Vehículo!)
# Estos son los superpoderes de OOP, ¡lo veremos luego!

# - HERENCIA 👨‍👩‍👧: Reutilización de código.
#   Una clase "hija" copia todo de una clase "madre".
#   Ej: La CLASE Auto y la CLASE Bicicleta NO tienen que definir 'color' o 'frenar()'.
#       Ellas HEREDAN esas propiedades y métodos directamente de la CLASE Vehiculo.
#       (Una CLASE VehiculosRuedas hereda de Vehiculo, y Auto/Bici heredan de VehiculosRuedas, ¡se pasa la posta!).

# - POLIMORFISMO 🎭: El mismo método hace cosas diferentes.
#   Significa "muchas formas". El método `acelerar()` existe en ambas clases, pero:
#   Ej: Auto.acelerar() mueve un motor a gasolina.
#   Ej: Bicicleta.acelerar() hace girar un par de piernas.
#   El método se llama igual (`acelerar`), pero se "personaliza" para cada clase, ¡eso es Polimorfismo!

#%%
# TODO: AGENDA DE CONTACTOS - EL MODO VIEJO (Procedimental)
# Así se haría sin OOP: datos sueltos (diccionarios) en una lista.
# Lo haremos así para ver POR QUÉ OOP es mejor.

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

# TODO: ACCEDER A LOS DATOS EN EL MODO VIEJO
# Es fácil, pero no hay *protección* de datos (cero validación).
# la lista contactos contiene diccionarios, cada uno es un contacto
print(contactos[0])    # Primer contacto: la caja completa

# para acceder a un valor específico usas la llave
print(contactos[0]['nombre'])    # Leemos la llave 'nombre'
print(contactos[0]['telefono'])  # Leemos la llave 'telefono'
print(contactos[0]['email'])     # Leemos la llave 'email'

#%%
# TODO: FUNCIONES PARA EL MODO VIEJO
# Fíjate que las funciones están separadas de la lista `contactos`.
# Si cambiamos la estructura de los diccionarios, ¡hay que cambiar TODAS estas funciones!

def agregar_contacto(contactos_list):
    # esta función pide datos al usuario y y crea un dicionario que agrega sobre una lista de contactos (argumento de entrada) 
    print("\nIngreso de contactos")
    print("------------------------")
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese telefono: ")
    email = input("Ingrese email: ")
    contactos_list.append({'nombre': nombre, 'telefono': telefono, 'email': email})
    return None

def listar_contactos(contactos_list):
    # esta función barre los elementos de la lista e imprime de forma enumerada los contactos
    print("\nInformacion de contactos")
    print("------------------------")
    for idx, contacto in enumerate(contactos_list, start=1):
        print(f"\nCONTACTO {idx}:")
        print(f"    Nombre: {contacto['nombre']}")
        print(f"    Telefono: {contacto['telefono']}")
        print(f"    Email: {contacto['email']}")

# # ejemplo de app con menú (OJO: Aquí los datos no se protegen)
# while True:
# #       print("\nAgenda de contactos")
# #       print("-----------------")
# #       print("[1] Agregar contacto")
# #       print("[2] Listar contactos")
# #       print("[0] Salir")
# #       opc = input("> : ")
# #       if opc == '0':
# #           break
# #       elif opc == '1':
# #           agregar_contacto(contactos)
# #       elif opc == '2':
# #           listar_contactos(contactos)
# #       else:
# #           print("Opcion invalida")

#%%
# TODO: CLASE Y OBJETO - Volvemos a la base
# CLASE = El molde/receta
# OBJETO = La cosa que creamos (INSTANCIA)

class Persona:
    pass    # 'pass' solo dice: "Aquí va código, pero ahora no tengo nada."

persona1 = Persona()
persona2 = Persona()

print(persona1)
print(persona2)
# ¿Por qué salen cosas raras? <__main__.Persona object at 0x...>
# Porque cada objeto es una cosa *única* en la memoria. Necesitamos __repr__ para que hablen claro.
# cada instancia (objeto) ocupa su propio espacio en memoria( persona )

#%%
# TODO: CONSTRUCTOR - __init__ y SELF (Inicializando la caja)
# El método `__init__` se llama automáticamente (es el constructor)
# justo cuando haces `Persona()`. Es el encargado de darle los datos iniciales.

# CLAVE: `self` es la referencia al *objeto* que se está construyendo AHORA.
class Persona:
    # self siempre va primero. Es el objeto `persona1` o `persona2` que se va a crear.
    def __init__(self):
        # Creamos el atributo interno (la propiedad) `_nombre`
        # y le damos el valor inicial 'NN' (Nombre No Asignado).
        # El guion bajo `_` es para decir: "Ojo, este dato es PRIVADO, usa Get/Set para tocarlo".
        self._nombre = 'NN'

#%%
# TODO: REPRESENTACIÓN - __repr__ vs __str__ (Haciendo que la caja hable)
# Estos métodos mágicos le dicen a Python cómo convertir el objeto en texto.

class Persona:
    def __init__(self):
        self._nombre = 'NN'
        
    def __str__(self):
        # __str__: Se llama automáticamente cuando usas `print(objeto)`.
        # Es para el USUARIO final.
        return "Objeto Persona - Print (Soy amigable)"

    def __repr__(self):
        # __repr__: Se llama cuando escribes el nombre del objeto en la terminal.
        # Es para el DESARROLLADOR (para hacer debugging, debe ser técnico).
        return "Objeto Persona - Representacion (Soy técnico)"

persona1 = Persona()
print(persona1) # Llama a __str__

# Si lo pones en la terminal sin print(), llama a __repr__
# >>> persona1
#%%
# MEJORA de __repr__ (¡Mostrando el estado real!)
# Normalmente definimos __repr__ para que nos muestre el valor actual del atributo.
# Así es útil para ver los datos internos del objeto.

class Persona:
    def __init__(self):
        self._nombre = 'NN'
    
    def __repr__(self):
        # Usamos .format() para inyectar el valor actual del atributo `self._nombre`
        return "Persona:[nombre:'{}']".format(self._nombre)
    
persona1 = Persona()
print(persona1) # Como no hay __str__, print() usa este __repr__.

# ¡Esta es la base perfecta antes de los setters/getters!
#%%
# TODO: SETTER - nos peremite asignar un valor a un atributo de la clase 
class Persona:
    #inicializamos el atributo con un vacio ''
    def __init__(self):
        self._nombre = ''
    def __repr__(self):
        return "Persona:[nombre:'{}']".format(self._nombre)
    
#camb iar el valor del atributo protegido ( _nombre)
#definimos un metodo que acepta 2 argumentos
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
# persona1.set_nombre(1234) # Esto dará error
# print(persona1)
            
            
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

#Acceder al valor del atribujo _nombre desde la terminal  
    def get_nombre(self):
        #Accedemos al atribujo interno y devuelve su valor actural 
        return self._nombre
    
    
# ejemplo rápido
persona1 = Persona()
persona1.set_nombre("Alan")
persona1.get_nombre()

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
        # Validamos que el nombre contenga caracteres y espacios en blanco
        if isinstance(val, str) and all([chars.isalpha() or chars.isspace() for chars in val]):
            self._nombre = val
        else:
            raise TypeError("El atributo 'nombre' debe de ser un objeto 'str' y contener solo letras y espacios")
            
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
        if isinstance(val, str) and '@' in val:
            self._email = val
        else:
            raise TypeError("El atributo 'email' debe de ser un objeto 'str' y contener un '@'")
            
    def get_email(self):
        return self._email

#%%
# INSTANCIAMIENTO DE UN OBJETO CLASE PERSONA Y PRUEBA DEL OBJETO
p1 = Persona()
p1.set_nombre("Alan Brito")
p1.set_telefono("987-282-821")
p1.set_email("alan@mail.com")

p1.get_nombre()
p1.get_telefono()
p1.get_email()

print(p1)
#%%
#verifiquemos excepciones 

# ESTA CELDA DEBERIA DE GENERAR UNA EXCEPCION (Prueba de Telefono)
try:
    p1_test_tel = Persona()
    print("--- Prueba: Teléfono con tipo 'int' ---")
    p1_test_tel.set_telefono(987112123)
except TypeError as e:
    print(f"✅ EXCEPCIÓN ESPERADA: {e}")

#%%
# ESTA CELDA DEBERIA GENERAR UNA EXCEPCION (Prueba de Email)
try:
    p1_test_email = Persona()
    print("--- Prueba: Email con tipo 'int' ---")
    p1_test_email.set_email(12345)
except TypeError as e:
    print(f"✅ EXCEPCIÓN ESPERADA: {e}")

#%%
def ingresar_contacto():
    contacto = Persona()
    contacto.set_nombre(input("Ingrese nombre: "))
    contacto.set_telefono(input("Ingrese telefono: "))
    contacto.set_email(input("Ingrese email: "))
    
    return contacto

# (La función duplicada se elimina)

def buscar_contacto(contactos_list):
    # El argumento "contactos" es una lista de Personas: [Persona(), Persona(), ...]
    found = False
    nombre = input("Ingrese el nombre del contacto: ")
    
    for contacto in contactos_list:
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
contactos = [p] # Renombro la lista para evitar conflicto con la procedimental

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
        except (ValueError, TypeError) as e:
            print(f"Ingreso inválido: {e}")
    elif opc == '2':
        buscar_contacto(contactos)
    elif opc == '3':
        listar_contactos(contactos)
    elif opc == '0':
        break
    else:
        print("Opcion invalida")
