   #!/usr/bin/env python3
# -*- coding: utf-8 -*-
#todo ver la linea 212 y entiendes todo 
# %%
# ============================================================================= 
# Programación Orientada a Objetos - Parte 2 OFICIAL 

# %%

# ¡La onda de Python con la POO es ser flexible! 🐍
# A diferencia de otros lenguajes más estrictos (como Java o C#),
# Python te deja hacer clases súper simples, casi sin reglas,
# o agregarles toda la seguridad que quieras si es necesario.
# Es parte de su filosofía de mantener el código simple y legible.

# %%
# =============================================================================
# ## The Python Way (La forma de hacer las cosas en Python)
# =============================================================================

# La idea clave es: "Confiamos en el programador".
# Por defecto, los atributos de una clase son PÚBLICOS, no privados.

# En otros lenguajes, para cambiar un nombre, harías algo "seguro" como:
# p1 = Persona()
# p1.set_nombre('Alan')   <-- Usar un método "setter"
# print(p1.get_nombre())  <-- Usar un método "getter"

# En Python, se prefiere la simpleza:
# p1 = Persona()
# p1.nombre = 'Alan'      <-- Asignación directa
# print(p1.nombre)        <-- Lectura directa

# Así que, vamos a definir la clase Persona de esta forma "simple".
# %%

# --- Clase Persona (Versión 1: Todo Público) ---
class Persona:
    """
    Un molde simple para crear personas.
    Versión 1: Todo público y directo.
    """
    def __init__(self):
        """
        El constructor. Se activa al crear la Persona (ej: p1 = Persona()).
        Simplemente prepara los "cajones" (atributos) vacíos.
        """
        self.nombre = ''
        self.telefono = ''
        self.email = ''
        
    def __repr__(self):
        """
        El método mágico de "representación".
        Le dice a Python cómo "imprimirse" bonito cuando haces print(obj).
        """
        return "Persona[nombre={}, telefono={}, email={}]".format(
            self.nombre, self.telefono, self.email)

# %%
# todo--- Prueba de la Clase Persona (Versión 1) ---

# Ojo: los atributos son `self.nombre` (público), no `self.__nombre` (privado).
# Así que podemos asignar y leer los atributos directamente.

print("--- Probando Persona v1 (Todo Público) ---")
p1 = Persona()
p1.nombre = 'Alan'  # Asignación directa. ¡Fácil!
p1.telefono = '987-273-362'
p1.email = 'alan@mail.com'

print(p1)

# Y podemos leerlos igual de fácil:
print(f"Leyendo el nombre: {p1.nombre}")
print(f"Leyendo el teléfono: {p1.telefono}")


# %%
# =============================================================================
# ## Setter y Getters como Decoradores (¡La solución!)
# =============================================================================

# ¡Ups! El problema de la "confianza total" es que perdimos el CONTROL.
# ¿Qué pasa si alguien hace esto?
# %%

# --- El Problema: Cero Control ---
print("\n--- Probando el Problema (Sin Control) ---")
try:
    print(f"El nombre ANTES es: {p1.nombre}")
    
    # ¡Aquí está el error! No hay control sobre el TIPO de dato.
    p1.nombre = 12345
    
    print(f"El nombre AHORA es: {p1.nombre}")
    print("¡ERROR! Python nos dejó asignar un número a un nombre. 😭")
except Exception as e:
    # Esta clase simple no lanza error, pero ponemos el try por si acaso
    print(f"Algo salió mal: {e}")

# %%
# Tenemos que recuperar el control (los setters) PERO sin perder
# la simpleza de `p1.nombre = 'Alan'`.
#
# todoLa solución: ¡Decoradores! (@property)
# todo Un Decorador es como "envolver" una función con otra para darle
# súper-poderes.
#
# Es como ponerle un 'guardia de seguridad' (@) a la puerta (el método)
# sin tener que cambiar la puerta en sí.
#
# Suena raro, pero mira qué útil es para getters y setters.
# %%
#TODO UN METODO MUCHO MEJOR ! 
#TODO
# --- Clase Persona (Versión 2: Con argumentos en __init__) ---
# Primero, un pequeño ajuste: pasemos los datos al crearla, no después.

class Persona:
    def __init__(self, nombre='', telefono='', email=''):
        # Esto todavía es asignación directa, ¡aún no hay setters!
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __repr__(self):
        return "Persona[nombre={}, telefono={}, email={}]".format(
            self.nombre, self.telefono, self.email)

print("\n--- Probando Persona v2 (con __init__ mejorado) ---")
p1_v2 = Persona('Alan', '987-373-173', 'alan@mail.com')
print(p1_v2)


# %%
# TODO--- Clase Persona (Versión 3: ¡La Solución "Pythonica" con Decoradores!) ---
# todo Ahora sí, agregamos el setter y getter para 'nombre'.
# ¡Presta mucha atención a esto!

class Persona:
    def __init__(self, nombre, telefono, email):
        # 1. ¡OJO! Cuando Python ve esto (`self.nombre = ...`),
        # ya NO lo guarda directamente en un atributo llamado 'nombre'.
        #TODO Ahora, ¡BUSCA y EJECUTA el 'setter' (@nombre.setter) de abajo!
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    @property               # <-- Este es el GETTER
    def nombre(self):
        """
        El GETTER (Obtenedor). Se activa cuando 'lees' el valor.
        (ej: `print(p1.nombre)`)
        
        Dice: "Oye, cuando alguien pida 'nombre', no busques un atributo.
        Ejecuta esta función y devuelve el valor que está en la variable 
        'privada' _nombre (con guion bajo)".
        """
        return self._nombre
    
    @nombre.setter          # <-- Este es el SETTER
    def nombre(self, var): # 'var' es el valor que intentas asignar (ej: 'Alan' o 12345)
        """
        El SETTER (Asignador). Se activa cuando 'escribes' un valor.
        (ej: `p1.nombre = 'Alan'`)
        
        Dice: "¡Alto ahí! Antes de guardar, ¡primero valida el valor (var)!"
        Es el guardia de seguridad.
        """
        # 2. La validación (el guardia):
        if isinstance(var, str):
            # 3. Si es un string, ¡adelante! Guárdalo en el atributo 'privado'.
            self._nombre = var  # Nótese el guion bajo (_)
        else:
            # 4. Si no, ¡lanza un error! No dejes que pasen datos malos.
            raise TypeError("El atributo 'nombre' debe ser un 'str'")
            
    # NOTA: Los otros atributos (telefono, email) siguen siendo públicos
    # y no tienen este control (por ahora).
    
    def __repr__(self):
        # 5. El __repr__ ahora llama al GETTER (@property)
        # automáticamente cuando pide 'self.nombre'.
        return "Persona[nombre={}, telefono={}, email={}]".format(
            self.nombre, self.telefono, self.email)

# %%
# todo--- Probando la Persona v3 (con Setters y Getters) ---
print("\n--- Probando Persona v3 (Con Setters/Getters) ---")

# Prueba 1: El camino feliz (funciona)
# (Se activa el Setter en el __init__)
p_segura = Persona("Ana", "123-456", "ana@mail.com")
print(f"Objeto creado: {p_segura}")

# (Se activa el Getter)
#ponemos el nombre modificado de la class.propiedad
print(f"Leyendo el nombre (usa el Getter): {p_segura.nombre}")

# Prueba 2: El camino triste (falla, ¡y eso es bueno!)
print("\nIntentando asignar un número al nombre...")
try:
    # (Se activa el Setter, pero fallará la validación)
    p_segura.nombre = 999
except TypeError as e:
    print(f"¡ÉXITO! El Setter nos protegió. Error: {e}")

print(f"El nombre sigue siendo (gracias al Getter): {p_segura.nombre}")

# %%
#todo =============================================================================
# #TODO Clase en Python: Caso practico (Circulo)
#todo =============================================================================
#todo Vamos a aplicar todo esto a una clase 'Circulo'.

# figuras.py  (from figuras import Circulo)
class Circulo:
    """
    ¡Un molde para crear objetos Círculo! 🔵
    
    Define un círculo usando dos cosas clave:
    1. Su radio (qué tan grande es).
    2. Su origen (dónde está su centro en un plano 2D, como (x, y)).
    """
    #DECLARAMOS NUESTAS CARACTERISTICAS 
    def __init__(self, radio=1, origen=(0, 0)):
        """
        El constructor.
        Cuando haces `self.radio = radio`, ¡se activa el SETTER de radio!
        Cuando haces `self.origen = origen`, ¡se activa el SETTER de origen!
        """
        self.radio = radio
        self.origen = origen
    
    def area(self):
        """Calcula y devuelve el área del círculo (PI * radio^2)"""
        return 3.1415 * self.radio ** 2
    
    def perimetro(self):
        """Calcula y devuelve el perímetro (2 * PI * radio)"""
        return 2 * 3.1415 * self.radio
    
    #TODO --- GETTER para Radio ---
    #TODO NOS SIRVE SOLO PARA ASEGURAR EL DATO U VALOR 
    @property
    def radio(self):
        """GETTER: Permite 'leer' el valor de `obj.radio`"""
        #TODO EN EL PROPERTY CUANDO RETORNAS TIENE QUE SER DIFERENTE, NO self.radio SINO SELF._RADIO
        return self._radio
    
    # --- GETTER para Origen ---
    @property
    def origen(self):
        """GETTER: Permite 'leer' el valor de `obj.origen`"""
        return self._origen
    
    # --- SETTER para Radio ---
   #TODO RECUERDA QUE EL SETTER ES PARA VALIDAD DATOS, NO RETORNAR , PARA RETORNAR ESTAN LAS FUNCIONES  
    @radio.setter
    def radio(self, val):
        """SETTER: Valida ANTES de 'escribir' en `obj.radio = val`"""
        if (isinstance(val, int) or isinstance(val, float)) and val > 0:
            # ¡Pasa el control! Lo guardamos en el atributo "real" _radio
            #todo EL DATO CAMBIADO OSEA EN ESTA CASO VAL TAMBIEN TIENE QUE IGUALAR A SELF._RADIO no a self.radio 
            self._radio = val
        else:
            # ¡No pasa! Lanzamos error.
            raise TypeError("La propiedad 'radio' debe ser un 'int' o 'float' mayor que 0")
    
    # --- SETTER para Origen ---
    @origen.setter
    def origen(self, val):
        """SETTER: Valida ANTES de 'escribir' en `obj.origen = val`"""
        if isinstance(val, tuple):
            # Es una tupla, ahora vemos adentro...
            if isinstance(val[0], int) or isinstance(val[0], float) and isinstance(val[1], int) or isinstance(val[1], float):
                # ¡Pasa el control!
                self._origen = val
            else:
                raise TypeError("Las coordandas de 'origen' debe ser numéricas")
        else:
            raise TypeError("La propiedad 'origen' debe ser una 'tuple'")
            
    
    # TODO--- Métodos de Acción (Acciones del Círculo) ---
    #CON LAS FUCNIONES PODEMOS RETORNAR O EJERCUTAR AR5CCIONES 
    # TODO  ESTE METODO ES MUY PRACTICO, COPY PAGE
    def mover_derecha(self, paso):
        """Mueve el círculo a la derecha sumando al eje X."""
        if isinstance(paso, int) or isinstance(paso, float):
            #TODO OJO: Esto llama al SETTER de 'origen'
            self.origen = (self.origen[0] + paso, self.origen[1])
        else:
            raise TypeError("El paso debe ser numerico")
    
    def mover_izquierda(self, paso):
        if isinstance(paso, int) or isinstance(paso, float):
            self.origen = (self.origen[0] - paso, self.origen[1])
        else:
            raise TypeError("El paso debe ser numerico")
    
    def mover_arriba(self, paso):
        if isinstance(paso, int) or isinstance(paso, float):
            self.origen = (self.origen[0], self.origen[1] + paso)
        else:
            raise TypeError("El paso debe ser numerico")
    
    def mover_abajo(self, paso):
        if isinstance(paso, int) or isinstance(paso, float):
            #PONGO SELF.ORIGEN[1] ESTE SERIA EL EJE Y 
            self.origen = (self.origen[0], self.origen[1]- paso)
        else:
            raise TypeError("El paso debe ser numerico")
    
    def expandir(self, paso):
        """Aumenta el radio. El SETTER de radio validará que siga > 0."""
        if isinstance(paso, int) or isinstance(paso, float):
            self.radio += paso
        else:
            raise TypeError("El paso debe ser numerico")
    
    def contraer(self, paso):
        """Reduce el radio, con una validación extra."""
        if isinstance(paso, int) or isinstance(paso, float):
            # Validamos ANTES de asignar, para un error más específico
            if self.radio - paso > 0:
                self.radio -= paso
            else:
                raise ValueError("El paso no debe de generar un radio negativo")
        else:
            raise TypeError("El paso debe der numerico")
    
    def esta_dentro(self, x, y):
        """Verifica si un punto (x, y) está dentro del círculo."""
        return (x - self.origen[0])**2 + (y - self.origen[1])**2 <= self.radio ** 2
    
    def __repr__(self):
        """Cómo se imprime el Círculo."""
        return "Circulo[radio={}, origen={}]".format(self.radio, self.origen)
    
    
    
def main_circulo_test():
    # --- Probando la clase Circulo ---
    print("\n--- Probando la Clase Circulo (con Setters) ---")
    try:
        c1 = Circulo(radio=2, origen=(0, 0))
        print(c1)
        #TODO SOLO LLAMA A LA FUNCION/ SON FUNCIONES QUE TE RETORNAN UN VALOR 
        print(f"Área: {c1.area()}")
        print(f"Perímetro: {c1.perimetro()}")
        print(f"¿Está (1, 1) adentro?: {c1.esta_dentro(1, 1)}")
        
        #TODO SE LLAMA A LA FUCNION DESDE AFUERA CUANDO ESTA REALIZA UNA ACCION 
        #TODO  CUANDO ESTA SOLAMENTE RETORNA UN VALOR LA PUEDES LLAMAR DESDE UN F-STRING
        c1.mover_abajo(1)
        print(f"\nDespués de mover abajo: {c1.origen}")
        print(f"¿Está (1, 1) adentro ahora?: {c1.esta_dentro(1, 1)}")
        
        # Prueba de error (radio negativo)
        print("\nIntentando crear Círculo con radio negativo...")
        c2 = Circulo(radio=-5)
        print(c2) # No debería llegar aquí
        
    except (TypeError, ValueError) as e:
        print(f"¡ÉXITO! El setter del Círculo nos protegió. Error: {e}")

# Ejecutamos la prueba del círculo
if __name__ == '__main__':
    main_circulo_test()


 # %%
# --- Creando muchos Círculos ---
from random import randint

print("\n--- Creando 10 Círculos Aleatorios ---")
circulos = []
for _ in range(10):
    # Creamos 10 círculos con radios y orígenes aleatorios
    circulos.append(Circulo(radio=randint(1, 10), origen=(randint(1, 10), randint(1, 10))))
                    
for circulo in circulos:
    print(circulo)


# %%
# =============================================================================
# ## Herencia y polimorfismo
# =============================================================================
#
# ¡Poder de familia! 👨‍👩‍👧‍👦
#
# HERENCIA: Es la capacidad de una clase "Hija" de recibir (heredar)
# todos los métodos y atributos de una clase "Padre".
# (Ej: Una Camisa ES Ropa, así que hereda 'usar()' y 'lavar()').
#
# POLIMORFISMO: (literalmente "muchas formas"). Es la capacidad
# de la clase "Hija" de REESCRIBIR (sobrescribir) un método del "Padre"
# para que se comporte diferente.
# (Ej: El __repr__ de Camisa es diferente al de Ropa, es más específico).
#
# %%

# --- Herencia: La Clase "Padre" (Ropa) ---
class Ropa:
    """
    El molde "Padre" o "Superclase".
    Define las cosas que TODA la ropa tiene en común.
    """
    def __init__(self, nombre='', estaLimpia=True, vecesUsada=0, maxUsos=1):
        self.nombre = nombre
        self.estaLimpia = estaLimpia
        self.vecesUsada = vecesUsada
        self.maxUsos = maxUsos
    
    def __repr__(self):
        """Cómo se imprime la Ropa."""
        return "Ropa[nombre={}, estaLimpia={}, vecesUsada={}, maxUsos={}]".format(self.nombre, 
                                                                                 self.estaLimpia,
                                                                                 self.vecesUsada, 
                                                                                 self.maxUsos)
    
    def usar(self):
        """La acción de usar la prenda."""
        self.vecesUsada += 1
        if self.vecesUsada >= self.maxUsos:
            # print(f"¡Ups! '{self.nombre}' ya está sucia.") # Opcional
            self.estaLimpia = False
        
    def lavar(self):
        """La acción de lavar la prenda."""
        # print(f"Lavando '{self.nombre}'... ¡Quedó como nueva!") # Opcional
        self.estaLimpia = True
        self.vecesUsada = 0

# %%
# --- Probando la clase Ropa ---
print("\n--- Probando la Clase Padre (Ropa) ---")
jean = Ropa('Blue Jean', maxUsos=5)
print(jean)

# Usando la ropa
print("\nUsando la ropa...")
for _ in range(5):
    # TODO ojo: LLAMAR A LA FUNCION ANTES 
    jean.usar()
    print(jean)
    
print("\nLavando la ropa...")
jean.lavar()
print(jean)

# %%
#TODO
# TODO--- Herencia: La Clase "Hija" (Camisa) ---

class Camisa(Ropa): # <-- ¡Aquí ocurre la Herencia! (Camisa hereda de Ropa)
    """
    El molde "Hijo" o "Subclase".
    Hereda TODO de Ropa (usar, lavar, __init__, etc.)
    Pero añade algo nuevo: 'cuello'.
    """
    def __init__(self, nombre='', estaLimpia=True, vecesUsada=0, maxUsos=1, cuello=16):
        
        # 1. ¡Llamamos al constructor del "Padre" (Ropa)!
        # `super()` es la forma de decir "mi súper-clase" (Ropa).
        # Le pasamos los atributos que él ya sabe manejar.
        #ESTOS SON LOS ATRIBUTOS QUE TENIA ROPA 
        super().__init__(nombre, estaLimpia, vecesUsada, maxUsos)
        
        # 2. Ahora, definimos el atributo NUEVO que solo 'Camisa' tiene.
        self.cuello = cuello
        
    def __repr__(self):
        # ¡POLIMORFISMO!
        # Sobreescribimos el __repr__ del padre para añadir el cuello.
        # Es "polimórfico" porque la misma función (print) llama a
        # diferentes métodos __repr__ según el objeto.
        return "Ropa[nombre={}, estaLimpia={}, vecesUsada={}, maxUsos={}, cuello={}]".format(self.nombre, 
                                                                                 self.estaLimpia,
                                                                                 self.vecesUsada, 
                                                                                 self.maxUsos,
                                                                                 self.cuello)

# %%
# --- Probando la Clase Hija (Camisa) ---
print("\n--- Probando la Herencia (Camisa) ---")
#todo maxUsos = 1 estamos indicado que el maximo de usos es 1 
camisa = Camisa("camisa tonera", maxUsos=1)
print(f"Recién creada: {camisa}")

# ¡Podemos usar métodos del "Padre" (Ropa) aunque estemos
# en un objeto "Hijo" (Camisa)!
camisa.usar()
print(f"\nDespués de usarla 1 vez: {camisa}")
print(f"¿Está limpia? {camisa.estaLimpia}")


# %%
# todo --- El poder del Polimorfismo en listas ---
#TODO EJERCICIO PRACTICO 
print("\n--- Guardando todo en el 'ropero' (una lista) ---")

ropero = []
ropero.append(Ropa(nombre='Polo Negro', maxUsos=3))
ropero.append(Camisa(nombre='Camisa Colegio', maxUsos=200)) # <-- Un objeto "Hijo"
ropero.append(Ropa(nombre='Jean Negro', maxUsos=8))
ropero.append(Ropa(nombre='Jean Azul', maxUsos=3))
ropero.append(Ropa(nombre='Media de rombos'))
ropero.append(Ropa(nombre='Polo deportivo', maxUsos=2))

# ¡Python no se hace problemas!
# Sabe que 'Camisa' ES-UN-TIPO-DE 'Ropa', así que los puede mezclar.
#
# Al imprimir, SÍ usa el __repr__ específico de cada uno.
# ¡Eso es Polimorfismo en acción!
for ropa in ropero:
    print(ropa)


# %%
# =============================================================================
# ##TODO  Más metodos mágicos (Dunders)
# =============================================================================
#
# Son esos métodos con doble guion bajo (`__dunder__`).
#TODO Le enseñan a tus objetos a usar operadores básicos (+, -, *, ==, >).
#
# * `__add__(self, other)` : Le enseña a tu objeto a 'sumar' (+)
# * `__sub__(self, other)` : Le enseña a tu objeto a 'restar' (-)
# * `__mul__(self, other)` : Le enseña a tu objeto a 'multiplicar' (*)
# * `__gt__(self, other)`  : Le enseña a tu objeto a 'comparar' (>) (Greater Than)
# * `__eq__(self, other)`  : Le enseña a tu objeto a 'ser igual' (==) (Equal)
# * `__floordiv__(self, other)`: Le enseña a usar la doble barra (//)

# %%
# --- Viendo los métodos mágicos de 'str' ---
print("\n--- Métodos mágicos de un 'str' (string) ---")
# Fíjate cuántos 'dunders' tiene un string.
# ¡Por eso puedes hacer 'a' + 'b'! (porque usa __add__)
# ¡Y por eso puedes hacer 'a' * 3! (porque usa __mul__)
# print(dir(str)) # Descomenta esto para ver la lista larga
print("... (muchos métodos como __add__, __mul__, __eq__, etc.) ...")


# %%
#TODO --- Ejemplo: Clase Círculo (Versión 2: con Métodos Mágicos) ---
#TODO OJO: Esta es una *nueva* definición de Círculo.
#TODO Es más simple (sin setters) para enfocarnos en la magia.

class Circulo:
    """Circulo v2: Con métodos mágicos para operadores."""
    
    def __init__(self, radio=1, origen=(0, 0)):
        self.radio = radio
        self.origen = origen
    
    def area(self):
        return 3.1415 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.1415 * self.radio

    #TODO --- Aquí empieza la magia ---
    
    def __add__(self, other):
        """Define qué pasa si haces: `circulo + numero`"""
        # print(f"Usando __add__ para sumar {other} al radio...")
        # Creamos un NUEVO círculo con el radio más grande.
        # 'other' es el número a la derecha del '+'
        return Circulo(radio=self.radio + other, origen=self.origen)
    
    def __mul__(self, other):
        """Define qué pasa si haces: `circulo * numero`"""
        # print(f"Usando __mul__ para multiplicar el radio por {other}...")
        # 'other' es el número a la derecha del '*'
        return Circulo(radio=self.radio * other, origen=self.origen)
    
    def __gt__(self, other):
        """
        Define qué pasa si haces: `circulo1 > circulo2` (Greater Than)
        Comparamos los radios.
        'other' es el objeto a la derecha del '>'
        """
        # print(f"Comparando {self.radio} >= {other.radio}...")
        return self.radio >= other.radio
            
    def __repr__(self):
        return "Circulo[radio={}, origen={}]".format(self.radio, self.origen)

# %%
# --- Probando los operadores mágicos del Círculo ---
print("\n--- Probando Círculo v2 (con Magia) ---")
c1 = Circulo()
print(f"Inicial: {c1}")

# Esto llama a c1.__add__(1)
c1 = c1 + 1
print(f"Después de + 1: {c1}")

# Esto llama a c1.__mul__(2)
c1 = c1 * 2
print(f"Después de * 2: {c1}")

# --- Probando la comparación ---
c_chico = Circulo(radio=1)
c_grande = Circulo(radio=10)

print(f"\nProbando comparaciones:")
# Esto llama a c_grande.__gt__(c_chico)
es_mas_grande = c_grande > c_chico
print(f"¿Es {c_grande} > {c_chico}?  Respuesta: {es_mas_grande}")

# Esto llama a c_chico.__gt__(c_grande)
es_mas_grande = c_chico > c_grande
print(f"¿Es {c_chico} > {c_grande}?  Respuesta: {es_mas_grande}")


# %%
# --- Caso Práctico Final: ¡Resistencias Eléctricas! ---
# Vamos a usar métodos mágicos para simular un circuito.
# %%

class Resistencia:
    """
    Define una resistencia eléctrica.
    Le enseñaremos a sumarse en serie (+) y en paralelo (//).
    """
    def __init__(self, valor=1, potencia=0.25):
        self.valor = valor # en Ohms
        self.potencia = potencia # en Watts
     
    def __add__(self, other):
        """
        Define la suma en SERIE: R_total = R1 + R2
        Se activa con el operador '+'
        """
        # print("Suma en serie (+)")
        return Resistencia(self.valor + other.valor)
    
    def __floordiv__(self, other):
        """
        Define la suma en PARALELO
        Se activa con el operador '//' (¡lo estamos reutilizando!)
        Fórmula: R_total = 1 / ( (1/R1) + (1/R2) )
        """
        # print("Suma en paralelo (//)")
        # Calculamos el inverso de la suma de los inversos
        req_inv = (1 / self.valor) + (1 / other.valor)
        return Resistencia(1 / req_inv)
    
    def __repr__(self):
        # {:.4f} formatea el número a 4 decimales
        return "Resistencia: Val={:.4f} Ohms".format(self.valor)

# %%
# --- Probando la clase Resistencia ---
print("\n--- Probando Resistencias Eléctricas ---")
r1 = Resistencia(100)
r2 = Resistencia(100)
print(f"R1: {r1}")
print(f"R2: {r2}")

# Esto llama a r1.__add__(r2) (Suma en Serie)
r_serie = r1 + r2
print(f"Serie (R1 + R2): {r_serie}") # Debería dar 200 Ohms

# Esto llama a r1.__floordiv__(r2) (Suma en Paralelo)
r_paralelo = r1 // r2
print(f"Paralelo (R1 // R2): {r_paralelo}") # Debería dar 50 Ohms

# ¡Podemos encadenar operaciones!
# 1. Se calcula (r1 // r2), que da una Resistencia de 50 Ohms
# 2. El resultado (50 Ohms) se suma (+) con r2 (100 Ohms)
# 3. El resultado final debe ser 150 Ohms
print("\nProbando operación combinada: (R1 // R2) + R2")
r_combinado = (r1 // r2) + r2
print(f"Combinado: {r_combinado}")

print("\n--- Fin del script ---")