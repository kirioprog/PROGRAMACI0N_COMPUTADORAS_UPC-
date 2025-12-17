# -*- coding: utf-8 -*-
# ==================================
# %% Semana 11: NumPy
# ==================================

# ---
# ¿Qué onda con NumPy?
# ---
# NumPy es como la navaja suiza de Python para todo lo que sea números.
# Le da a Python "superpoderes" para manejar listas de números (vectores)
# y tablas (matrices) de forma súper rápida.

# ---
# El "Stack" Científico de Python
# ---
# NumPy no anda solo, es el cimiento de un montón de herramientas geniales:
#
# * numpy: El mero-mero, da el soporte para "arreglos" (arrays) y matrices.
# * matplotlib: Para hacer gráficas (2D y 3D) que se vean pros.
# * pandas: El jefe para analizar y limpiar datos (como tablas de Excel).
# * scipy: Para matemática más avanzada y cosas de ingeniería.
#
# Piensa en NumPy como los cimientos de una casa. No los ves, pero
# sin ellos, pandas y matplotlib se caerían.
#
#todo  Para usarlo, SIEMPRE lo importamos con el alias 'np'. Es la ley.
# ---

# pip install numpy  # (Esto solo lo haces una vez en tu terminal)
import numpy as np

# ---
# ¿Por qué usar 'arrays' de NumPy y no listas normales de Python?
# ---
# Buena pregunta. Veamos un ejemplo. Digamos que tenemos esta lista
# de temperaturas en grados Centígrados.
# ---

temp_C = [26.8, 29.4, 30.1, 29.5, 28.6, 29.9, 28.4]

# ---
# Queremos convertir toda la lista a Fahrenheit.
# La fórmula es: F = (9/5) * C + 32
#
# Con listas normales de Python, la cosa se complica...
# ---

print("\n--- Conversión con Bucle 'for' ---")
# Forma 1: El bucle 'for' (El camino largo)
temp_F = []
for temp in temp_C:
    temp_F.append(9/5 * temp + 32)
    
print(temp_F)
#%%
# ---
# Funciona, pero es mucho código. Podemos usar una "list comprehension".
# Es más "Pythonico", más elegante.
# ---

print("\n--- Conversión con List Comprehension ---")
# Forma 2: List Comprehension (Más cool)
temp_F = [9/5 * temp + 32 for temp in temp_C]
print(temp_F)

# ---
# O con la función `map`, que es más "funcional" (y un poco más rara).
# ---

print("\n--- Conversión con 'map' y 'lambda' ---")
# Forma 3: Con 'map' (Para los que les gusta lo funcional)
temp_F = list(map(lambda x: 9/5 * x + 32, temp_C))
print(temp_F)

#%%
# ==================================
#todo %% La Ventaja Real: El Arreglo de NumPy
# ==================================
#todo Ahora veamos cómo se hace con NumPy.
# Primero, creamos un 'array' (arreglo) a partir de nuestra lista.
# ---
temp_C = [26.8, 29.4, 30.1, 29.5, 28.6, 29.9, 28.4]

print("\n--- Creando nuestro primer Array ---")
#todo IMPORTANTE CONVERTIR UNA LISTA EN ARRAY NUMPY
array_C = np.array(temp_C)
print(array_C)
print(type(array_C))  # Fíjate, ya no es 'list', es 'ndarray'

# ---
# Ahora, la magia. Apliquemos la fórmula DIRECTO al arreglo.
# ---

print("\n--- Conversión con NumPy (¡Facilísimo!) ---")
array_F = 9/5 * array_C + 32
print(array_F)

# La gran ventaja es la VELOCIDAD.
# NumPy está escrito en C por debajo, así que es rapidísimo.
# Vamos a probarlo con 1 millón de temperaturas.
# ---

print("\n--- Preparando prueba de velocidad (1 millón de datos) ---")
#IMPORTAMOS LA FUNCION UNIFORM DE LA LIBRERIA RANDOM 
from random import uniform

# Generamos una lista ENORME de Python
temp_C_grande = [uniform(20, 30) for _ in range(1000000)]
print(f"Lista creada con {len(temp_C_grande)} elementos.")
# print("{}{},{}..., numero de elementos: {}".format(temp_C[0], temp_C[1], temp_C[2], len(temp_C)))


print("\n--- Prueba 1: Bucle 'for' (lento) ---")
# %%time  
# La línea de arriba (%%time) es un "comando mágico" de Jupyter.
# Mide cuánto tarda en ejecutarse el código de abajo./ SOLO FUNCIONA EN JUPYTER

temp_F = []
for temp in temp_C_grande:
    temp_F.append(9/5 * temp + 32)
print("Prueba 'for' terminada.")


print("\n--- Prueba 2: 'map' (menos lento) ---")



# %% Arreglos 1-D (Vectores)
# ==================================
# Empecemos por lo básico: arreglos de una dimensión (como una lista).
# Soportan las mismas "rebanadas" (slicing) que las listas.
# ---

print("\n--- Jugando con Arreglos 1D (Slicing) ---")
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#todofunciona practicamente como una lista, podemos llamar un elemento de cualquier posicion 
print(f"Arreglo A: {A}")
print(f"A[0]: {A[0]}")      # El primero
print(f"A[-1]: {A[-1]}")     # El último
print(f"A[::2]: {A[::2]}")   # De 2 en 2

# ---
#todo Ahora, ojo con esto. Asignar valores...
# ---

print("\n--- Asignación de valores y Tipos de Datos ---")
A[0] = 100
print(f"A (con A[0]=100): {A}")

# ¡OJO AQUÍ!
# El arreglo A se creó con números ENTEROS (int).
# Si intentas meter un decimal (float)...
A[-1] = 10.5
print(f"A (con A[-1]=10.5): {A}")
#todo  ¿Viste? ¡Lo redondeó a 10! NumPy no mezcló tipos.

# Y si intentas meter un texto (string)...
try:
    print("Intentando A[-1] = 'a'...")
    A[-1] = 'a' # Esto va a fallar
    print(A)
except ValueError as e:
    print(f"¡ERROR! {e}")
    print("Como ves, no puedes mezclar peras con manzanas.")
    print("El arreglo es de 'int' y no acepta un string.")

# ---
# ¿Por qué pasó eso?
#TODO A diferencia de las listas de Python, los arreglos de NumPy son
#TODO **homogéneos**: todos sus elementos DEBEN ser del mismo tipo.
# (int32, float64, etc.). 
#
# Esto es CLAVE para que sean rápidos. Saben exactamente cuánta
# memoria ocupa cada elemento y no tienen que andar preguntando.
#
# NumPy tiene CIENTOS de funciones. No intentes aprenderlas todas.
# Vamos a ver las propiedades más importantes de un arreglo.
# ---

#TODO print("\n--- ¿Qué tanto trae NumPy? (dir(np)) ---")
# dir(np)  # Descomenta esto si quieres ver la lista GIGANTE de funciones

# ---
#TODO Propiedades clave de un 'ndarray' (el objeto arreglo):
##TODO FUNCIONES IMPORTANTES
# * array.size: ¿Cuántos elementos tiene en total?
# * array.ndim: ¿Cuántas dimensiones tiene? (ej. 1D, 2D, 3D)
# * array.shape: La "forma". (ej. una tupla (3, 4) -> 3 filas, 4 columnas)
# * array.dtype: El "tipo de dato" (ej. int32, float64)
# * array.itemsize: ¿Cuántos bytes ocupa cada elemento?
# ---

print("\n--- Propiedades de un Arreglo ---")
# Vamos a forzar que el arreglo sea de tipo 'float32' / osea cada dato sera de tipo float y ocupara 32 bits
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32)   # dtype=np.<tipo de datos numpy> : dtype=np.float64

print(f"Arreglo A: {A}")
print(f"Num de elementos (A.size): {A.size}")     # ¡Usa .size, no len(A)!
print(f"Dimensiones (A.ndim): {A.ndim}")
print(f"Forma (A.shape): {A.shape}")               # (9,) -> una tupla con un solo valor
print(f"Tipo de dato (A.dtype): {A.dtype}")
print(f"Bytes por elemento (A.itemsize): {A.itemsize}")
#%%
# ---
#todo ¡IDEA CENTRAL DE NUMPY!
#
#todo **Los métodos de NumPy SIEMPRE crean arreglos nuevos.**
#todo
# No modifican el original (casi nunca).
#
# Ejemplo:
# En listas de Python: L.append(val) -> Modifica L
# En NumPy: A = np.append(A, val) -> Crea un *nuevo* A con el valor
#
# Tienes que re-asignar la variable. ¡Interioriza esto!
# ---

print("\n--- La idea central: np.append ---")
#todo Los metodos de numpy crean nuevos arreglos
print(f"A original: {A}")
A = np.append(A, 10)
print(f"A después de append: {A}")

# ---
# Otros ejemplos de métodos que crean arreglos nuevos:
# ---

print("\n--- np.insert ---")
#tododonde ve el 3, ahi le va a seguir el 0,0,0
A = np.insert(A, 3, [0, 0, 0])
print(f"A después de insert: {A}")


print("\n--- np.delete ---")
#todonos quita el ultimo elemento del array
A = np.delete(A, -1)
print(f"A después de delete: {A}")
#%%
# ==================================
#todo %% Creación de Arreglos
# ==================================
#todo ¿Y si no tengo una lista? ¿Cómo creo arreglos de cero?
#
#todo Método 1: `np.arange` (como el `range` de Python, pero con esteroides)
# ---

print("\n--- Creando arreglos con np.arange ---")
A = np.arange(10)   # creamos un array que va del 0 al 9 (del 0 al 9)
print(A)


A = np.arange(1, 50, 3) # Del 1 al 49, en pasos de 3
print(A)


# ¡A `arange` SÍ le gustan los pasos decimales! (a `range` no)
A = np.arange(1, 5, 0.25)   #todo arange soporta valores de paso tipo float
print(A)

#%%
# Esto es súper útil cuando sabes el "paso" o "intervalo" que quieres.
# Ejemplo: Calcular la distancia de un carro cada 0.5 segundos.
# ---

print("\n--- Ejemplo `arange`: Movimiento Acelerado ---")
# Movimiento acelerado uniforme. Aceleración de 1.3 m/s**2
# d = 0.5 * a * t^2
a = 1.3
t = np.arange(0, 10.5, 0.5) # Instantes de tiempo entre 0 y 10 seg en pasos de 0.5 seg
d = 0.5 * a * t**2

print("   TIEMPO     DISTANCIA")
print("   ------     ---------")
#TODO `zip` nos deja iterar sobre 't' y 'd' al mismo tiempo
for val_t, val_d in zip(t, d):
    print("{:>6.2f} seg   {:>6.2f} m".format(val_t, val_d))

#%%
# Método 2: #TODO`np.linspace` (espacio lineal)
#
# Esto es diferente. Aquí no le dices el "paso", le dices:
#TODO "Dame [N] números exactos entre [inicio] y [fin]".
#
# Es perfecto cuando no te importa el paso, sino cuántos puntos quieres.
#TODO Por defecto, `linspace` divide el rango en 50 partes.
# ---

print("\n--- Creando arreglos con np.linspace ---")
A = np.linspace(0, 10)  # 50 valores entre 0 y 10 (incluye el 10)
print(A)


A = np.linspace(0, 100, 12)   # 12 valores exactos entre 0 y 100
print(A)

#%%
# Ejemplo: Queremos 6 mediciones de distancia, sin importar el intervalo.
# ---

print("\n--- Ejemplo `linspace`: 6 mediciones ---")
# Ejemplo
a = 1.3
t = np.linspace(0, 10, 6)   # 6 instantes de tiempo entre 0 y 10 seg
d = 0.5 * a * t**2

print("   TIEMPO     DISTANCIA")
print("   ------     ---------")
for val_t, val_d in zip(t, d):
    print("{:>6.2f} seg   {:>6.2f} m".format(val_t, val_d))

#%%
#TODO Método 3: `np.logspace` (espacio logarítmico)
#
#TODO Igual que linspace, pero la escala es logarítmica (potencias de 10).
#TODO np.logspace(0, 2, 10) -> Dame 10 números entre 10^0 (1) y 10^2 (100).
# ---

print("\n--- Creando arreglos con np.logspace ---")
A = np.logspace(0, 2, 10)  # Espaciamiento logaritmico de 10^0 hasta 10^2 (10 elementos)
print(A)


#%% ==================================
#todo  Arreglos n-dimensionales (Matrices)
# ==================================
#todo Ahora, el verdadero poder: arreglos de 2 dimensiones (tablas/matrices).
#todo Los creamos con una "lista de listas".
# ---

print("\n--- Arreglos 2D (Matrices) ---")
#2 dimensiones, 2 llaves 
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A)

print("\n--- Propiedades del Arreglo 2D ---")
print("Num de elementos:", A.size)     # 3 * 4 = 12
print("Dimensiones:", A.ndim)       # 2 dimensiones
print("Rango:", A.shape)            # (3, 4) -> 3 filas, 4 columnas
print("Tipo de dato", A.dtype)
print("Bytes de memoria por elemento:", A.itemsize)

# ---
# Para 2D, el "slicing" es más pro.
# Usamos la sintaxis [fila, columna]
# ---

print("\n--- Slicing en 2D [fila, columna] ---")
print(f"A[2, 0]: {A[2, 0]}")   # [fila, columna]: 9
print(f"A[:, 0]: {A[:, 0]}")   # Todas las filas, columna 0: [1 5 9]
print(f"A[1, :]: {A[1, :]}")   # [5 6 7 8]
print(f"A[:, ::2]:\n{A[:, ::2]}")    # [todas las filas, todas las columnas en pasos de 2]
print(f"A[::2, ::2]:\n{A[::2, ::2]}")  # [filas de 2 en 2, columnas de 2 en 2]
print(f"A[-1, ::-2]: {A[-1, ::-2]}")  # [12 10]
print(f"A[[0, 2], [1]]: {A[[0, 2], [1]]}") # [2 10] (Esto es "indexing" avanzado)

# ---
# ¿Y 3D? (Cubos de datos)
# Pues lo mismo: una lista, de listas, de listas...
# ---

print("\n--- Arreglos 3D (Cubos) ---")
#3 dimensiones 3 llaves 
A = np.array([[[1, 2, 3, 4]], [[5, 6, 7, 8]], [[9, 10, 11, 12]]])
print(A)

print("\n--- Propiedades del Arreglo 3D ---")
print("Num de elementos:", A.size)     # 12
print("Dimensiones:", A.ndim)       # 3 dimensiones
print("Rango:", A.shape)            # (3, 1, 4)
print("Tipo de dato", A.dtype)
print("Bytes de memoria por elemento:", A.itemsize)

#%%
# ==================================
#todo %% Creación de Arreglos n-D: `reshape`
# ==================================
# Es un dolor de cabeza crear matrices con listas de listas.
#todo
#todo El truco es usar `arange` (para crear 1D) y luego `reshape`
#todo (para "darle forma").
# ---

print("\n--- Creando matrices con `arange` y `reshape` ---")
# Se genera un arreglo de 12 elementos (1 a 12) y luego se le da la forma de 4x3
A = np.arange(1, 13).reshape(4, 3)       # arr.reshape(nfil, ncol)
print(A)


# ==================================
# %% Operaciones n-D: El concepto de `axis` (eje)
# ==================================
# ¡ESTO ES LO MÁS IMPORTANTE Y CONFUSO DE NUMPY!
#
# Cuando tienes una matriz, ¿las operaciones se hacen "hacia abajo"
# (por columnas) o "hacia los lados" (por filas)?
#
# Eso lo define el parámetro `axis` (eje).
#
# En una matriz 2D:
# * axis=0 -> Opera "a lo largo de las FILAS" (es decir, verticalmente).
# * axis=1 -> Opera "a lo largo de las COLUMNAS" (es decir, horizontalmente).
#
# Piénsalo como: "el eje que va a COLAPSAR".
# Si colapsas las filas (axis=0), te queda un resultado por columna.
# Si colapsas las columnas (axis=1), te queda un resultado por fila.
#
#todo Veamos `insert`.
# ---

print("\n--- Jugando con `axis` (ejes) ---")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A, '\n')

# axis=0 -> Inserta como una nueva FILA en la pos 1
#todo en la fila siguiente al numero 1 
A = np.insert(A, 1, [100, 200, 300, 400], axis=0)
print(A, '\n')

# axis=1 -> Inserta como una nueva COLUMNA en la pos 2
A = np.insert(A, 2, [0, 0, 0, 0], axis=1)
print(A, '\n')

#todo axis=0 -> Borra la FILA en la pos 1
A = np.delete(A, 1, axis=0)
print(A, '\n')

#%%
#TODO Lo mismo pasa con `concatenate` (pegar matrices).
# ¿Las pegas una encima de la otra (axis=0) o una al lado de la otra (axis=1)?
# ---

print("\n--- Concatenar matrices (pegar) ---")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A, '\n')

#TODO Apila A sobre sí misma (crece verticalmente)
A = np.concatenate([A, A], axis=0)
print(A, '\n')

#TODO Apila A (que ya es doble) al lado de sí misma (crece horizontalmente)
A = np.concatenate([A, A], axis=1)
print(A, '\n')

#%%
# El `axis` también es CLAVE para las operaciones matemáticas
# como `sum`, `mean` (promedio), `max`, etc.
#
# Regla fácil (la del "colapso"):
# `np.sum(A, axis=0)` -> Suma "hacia abajo" (colapsa filas). Devuelve la su ma DE CADA COLUMNA.
# `np.sum(A, axis=1)` -> Suma "hacia los lados" (colapsa columnas). Devuelve la suma DE CADA FILA.
# `np.sum(A)` (sin axis) -> Suma TODO. Devuelve un solo número.
# ---

print("\n--- Operaciones con `axis` (ej. `sum`) ---")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A, '\n')

print(f"Suma TOTAL (sin axis): {np.sum(A)}\n")            # A.sum() (NO SE RECOMIENDA)

# Regla: "axis=0" opera verticalmente, da un resultado POR COLUMNA.
# (1+5+9), (2+6+10), (3+7+11), (4+8+12) -> [15 18 21 24]
print(f"Suma en axis=0 (suma de columnas): {np.sum(A, axis=0)}\n")

# Regla: "axis=1" opera horizontalmente, da un resultado POR FILA.
# (1+2+3+4), (5+6+7+8), (9+10+11+12) -> [10 26 42]
print(f"Suma en axis=1 (suma de filas): {np.sum(A, axis=1)}\n")


# ---
# Sí, es confuso. Pero la regla de "colapsar" ayuda.
#
#TODO Aquí hay un montón de funciones matemáticas útiles de NumPy.
#TODO Fíjate que casi todas son `np.funcion(arreglo)`.
# ---

print("\n--- Métodos matemáticos útiles (1D) ---")
# Metodos utiles de Numpy
A = np.array([1, 2, 3, 4, 5])
print(f"np.sum(A): {np.sum(A)}\n")      # Suma
print(f"np.max(A): {np.max(A)}\n")      # Máximo
print(f"np.min(A): {np.min(A)}\n")      # Mínimo
print(f"np.mean(A): {np.mean(A)}\n")     # Promedio (media)
print(f"np.median(A): {np.median(A)}\n") # Mediana
print(f"np.prod(A): {np.prod(A)}\n")     # Producto (1*2*3*4*5)
print(f"np.cumsum(A): {np.cumsum(A)}\n") # Suma acumulada [1, 1+2, 1+2+3, ...]
print(f"np.cumprod(A): {np.cumprod(A)}\n")# Producto acumulado

# Operaciones básicas en numpy
print(f"np.sqrt(A): {np.sqrt(A)}\n")    # Raíz cuadrada de cada elemento
print(f"np.sin(A): {np.sin(A)}\n")    # Seno de cada elemento
print(f"np.log(A): {np.log(A)}\n")    # Logaritmo natural de cada elemento

# Valores en numpy
print(f"np.pi: {np.pi}")


#%%
#TODO Números Aleatorios con NumPy
# ==================================
# ¿Recuerdas lo que tardó crear la lista de 1 millón?
#TODO El módulo `np.random` es súper rápido y crea arreglos
# aleatorios directamente.
# ---

print("\n--- Generación de Arreglos Aleatorios ---")
# OJO: La "forma" (shape) se pasa como una tupla.
# Las dimensiones del arreglo resultante se especifican en una tupla

# 5 números aleatorios (float) entre 0 y 1
A = np.random.random((5,))  
print(f"np.random.random((5,)): \n{A}\n")

# Una matriz de 5x4 aleatoria (float) entre 0 y 1
A = np.random.random((5, 4))
print(f"np.random.random((5, 4)): \n{A}\n")

#todo Una matriz de 2x4 aleatoria (int) entre 1 y 9 (10 no incluido)
A = np.random.randint(1, 10, (2, 4))     # randrange -> randint
print(f"np.random.randint(1, 10, (2, 4)): \n{A}\n")

# Una matriz de 3x5 aleatoria (float) entre 1 y 5
A = np.random.uniform(1, 5, (3, 5))
print(f"np.random.uniform(1, 5, (3, 5)): \n{A}\n")


 # %% 
#TODO Indexación Booleana (¡El Súper-Poder de NumPy!)
# ==================================
#TODO Esta es, quizás, la herramienta más poderosa para análisis de datos.
#
# En lugar de pedir `A[5]` (el índice 5),
#TODO puedes pedir `A[A > 5]` (¡dame todos los elementos de A que sean > 5!)
#
# ¿Cómo funciona?
# 1. Creas una condición (ej. A % 2 == 0)
# 2. NumPy te devuelve un arreglo de `True` y `False` (una "máscara")
# ---

print("\n--- Indexación Booleana: La 'Máscara' ---")
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# ¿Cuáles elementos son pares?
mascara_pares = (A % 2 == 0)
print(f"Arreglo A: {A}")
print(f"Máscara (A % 2 == 0): {mascara_pares}")

# ---
# 3.-#todo Usas esa "máscara" como si fuera un índice.
# NumPy te devolverá SÓLO los elementos donde la máscara era `True`.
# ---

print("\n--- Aplicando la Máscara (Filtrando) ---")
#todo "De A, dame solo los elementos donde la máscara es True"
A_pares = A[mascara_pares]
# O, más directo:
# A_pares = A[A % 2 == 0]
print(f"A[A % 2 == 0]: {A_pares}") # CREO QUE ES EL MAS CLARO, SOLO SE IMPRIMEN LOS QUE SON MULTIPLOS DE 2

# ---
# ¡Esto es brutalmente útil!
# Ejemplo: Tenemos 31 días de temperaturas.
# Queremos filtrar datos SIN USAR BUCLES 'FOR'.
# ---

print("\n--- Ejemplo de Filtrado Booleano: Temperaturas ---")
temp_Ene = np.random.uniform(24, 32, (31,)) # 31 temps
print(f"Temperaturas Enero (primeros 5): {temp_Ene[:5]}...\n")

print("Temperaturas por encima de 30 grados")
print(temp_Ene[temp_Ene > 30], '\n')

print("Temperaturas por encima de promedio del mes")
promedio_mes = np.mean(temp_Ene)
print(f"(Promedio: {promedio_mes:.2f})")
print(temp_Ene[temp_Ene > promedio_mes], '\n')

print("Temperaturas entre 28 y 29 grados")
# OJO: Para 'y' (AND) se usa '&'
#      Para 'o' (OR) se usa '|'
# ¡Y los paréntesis son OBLIGATORIOS!
mascara_rango = (temp_Ene >= 28) & (temp_Ene <= 29)
print(temp_Ene[mascara_rango], '\n')    #, &, |, !=

# ---
#todo ¿Y si no quiero los VALORES, sino los ÍNDICES (posiciones)?
#
#todo Para eso usamos `np.where(condicion)`.
# "Dime DÓNDE (where) se cumple esta condición".
# ---

print("\n--- Buscando Índices con `np.where` ---")
# ¿En qué posiciones (índices) están los números pares?
A_indices_pares = np.where(A % 2 == 0)
print(f"np.where(A % 2 == 0): {A_indices_pares}")
print(f"Tipo de resultado: {type(A_indices_pares)}")

# ---
# ¡OJO! `where` devuelve una TUPLA.
# ¿Por qué? Porque si la matriz fuera 2D, devolvería
# (array_de_filas, array_de_columnas).
#
# Para 1D, el array que queremos está en la posición [0] de la tupla.
#
# Ejemplo: ¿Qué DÍAS (índices) hizo calor?
# ---

print("\n--- Ejemplo `np.where`: Días con temp entre 28-29 ---")
# Ejemplo
temp_Ene = np.random.uniform(24, 31, (31,))
print(f"Temperaturas Enero (primeros 5): {temp_Ene[:5]}...")

# 1. La condición
condicion = (temp_Ene >= 28) & (temp_Ene <= 29)

# 2. Obtener los índices
dias = np.where(condicion)

# 3. Acceder al array de índices (el [0])
print()
for dia_idx in dias[0]:
    # Sumamos 1 al índice (día 0 es día 1)
    dia_real = dia_idx + 1
    temp_ese_dia = temp_Ene[dia_idx]
    print(f"Ene {dia_real:2}: {temp_ese_dia:.2f}°C")
    # print("Ene {:2}: {:.2f}°C".format(dia, temp_Ene[dia-1])) # Forma original


# ==================================
# %% Ejemplo de Aplicación 1: Fricción
# ==================================
#
# Calcular el coeficiente de fricción (mu)
# mu = F / (m * g)
# g = 9.81 m/s^2
#
# Tenemos 6 experimentos:
# Masas (kg): [ 2,  4,  5, 10,  20,  50]
# Fuerza (N): [12.5, 25.5, 30, 61, 118, 294]
#
# Queremos el coeficiente medio de todos.
# ---

print("\n--- Solución Ejemplo Fricción ---")

# import numpy as np  # Ya está importado
g = 9.81
m = np.array([2, 4, 5, 10, 20, 50])
F = np.array([12.5, 25.5, 30, 61, 118, 294])

# ¡La magia de NumPy! La fórmula es idéntica.
mu = F / (m * g)

print(f"Coeficientes individuales: {mu}")
print(f"Coeficiente medio: {np.mean(mu)}")


# ---
# ¡Otro descanso! Ya casi...
# ---


#%%
#todo  %% BONUS TRACK: El objeto `np.matrix`
# ==================================
#
# NumPy tiene un objeto especial `matrix` (además de `array`).
#
# **ADVERTENCIA:** La comunidad de NumPy y Pandas
# **NO RECOMIENDA USAR `np.matrix`**.
#
# Se prefiere usar `np.array` para TODO.
#
# `np.matrix` se comporta más como MATLAB, pero es menos flexible
# y puede ser confuso. Lo vemos solo para que sepas que existe.
# ---

print("\n--- El objeto `np.matrix` (No muy recomendado) ---")
M = np.matrix(np.arange(1, 13).reshape(4, 3))
print(M, '\n')
print(f"Tipo: {type(M)}")

# ---
# La principal diferencia es que `*` significa
# MULTIPLICACIÓN DE MATRICES, no multiplicación elemento-a-elemento.
# ---

print("\n--- Multiplicación de Matrices (A*B != B*A) ---")
M1 = np.matrix(np.random.randint(1, 10, (3, 1))) # 3x1
M2 = np.matrix(np.random.randint(1, 10, (1, 3))) # 1x3

print("M1 (3x1) =\n", M1, '\n')
print("M2 (1x3) =\n", M2, '\n')

# M1 * M2 -> (3x1) * (1x3) = (3x3)
print("M1 * M2 (3x3) =\n", M1 * M2, '\n')

# M2 * M1 -> (1x3) * (3x1) = (1x1)
print("M2 * M1 (1x1) =\n", M2 * M1)

# (En `np.array`, esto se haría con `np.dot(A, B)` o `A @ B`)

# ---
# `np.matrix` tiene atajos útiles para álgebra lineal,
# como `.I` (Inversa) y `.T` (Transpuesta).
# ---

print("\n--- Atajos de Álgebra Lineal en `np.matrix` ---")
M = np.matrix(np.random.randint(1, 10, (3, 3)))
print(M, '\n')

try:
    # Inversa (M.I)
    print(f"Inversa (M.I):\n{M.I}\n")
except np.linalg.LinAlgError:
    print("¡La matriz no tiene inversa (singular)!\n")

# Transpuesta (M.T)
print(f"Transpuesta (M.T):\n{M.T}\n")

# Determinante (esto usa `np.linalg`, no es un atajo)
print(f"Determinante (np.linalg.det(M)): {np.linalg.det(M)}\n")


# ---
# Notación MATLAB para definir matrices
# ---
# `np.matrix` también acepta un string (texto) para definirse,
# muy al estilo de MATLAB (',' para columnas, ';' para filas).
#
# Esto es útil si copias y pegas de MATLAB.
#
# Ejemplo: Resolver un sistema de ecuaciones
#
# 2x + 3y - 2z = 8
# 1x + 0y - 4z = 1
# 2x - 1y + 6z = 4
#
# En forma matricial: A * X = B
# La solución es: X = A_inversa * B
# ---

print("\n--- Resolver Sistema de Ecuaciones (Estilo MATLAB) ---")
# Notación de string:
A = np.matrix("2, 3, -2; 1, 0, -4; 2, -1, 6")
B = np.matrix("8; 1; 4")      # [[8], [1], [4]]

# Se calcula Inv(A) * B
X = A.I * B

print(f"Solución X (x, y, z):\n{X}\n")
print(f"Tipo de X: {type(X)}")


# ==================================
# %% Ejemplo de Aplicación 2: Notas de Alumnos
# ==================================
# Simular las notas de 15 alumnos con 5 evaluaciones.
#
# Queremos:
# 1. Promedio por alumno
# 2. Promedio por evaluación
# 3. Número total de aprobados (promedio >= 10.5)
# ---

print("\n--- Solución Ejemplo Notas ---")
# import numpy as np # Ya importado

# 1. Simular notas (15 filas, 5 columnas) de 5 a 18
notas = np.random.randint(5, 19, (15, 5))

# 2. Promedio por alumno
# Queremos colapsar las columnas (evaluaciones) -> axis=1
# Usamos .reshape(15, 1) para que sea un vector columna (15x1)
prom_alumnos = np.mean(notas, axis=1).reshape(15, 1)

# 3. Promedio por evaluación
# Queremos colapsar las filas (alumnos) -> axis=0
# Esto da un vector fila (1x5)
prom_evaluaciones = np.mean(notas, axis=0)

# 4. Número de aprobados
# Usamos indexación booleana sobre los promedios
num_aprob = prom_alumnos[prom_alumnos >= 10.5].size

# --- Impresión de Resultados ---

# Para imprimir bonito, pegamos los promedios (15x1)
# al lado de las notas (15x5) -> (15x6)
data_notas = np.concatenate([notas, prom_alumnos], axis=1)

print("ALUMNO        N1    N2    N3    N4    N5    PROM")
print("=================================================")
for idx, notas_alum in enumerate(data_notas):
    # *notas_alum "desempaca" el arreglo [n1, n2, n3, n4, n5, prom]
    # en 6 argumentos separados para el .format()
    print("Alumno {:2}: {:5.0f} {:5.0f} {:5.0f} {:5.0f} {:5.0f}    {:5.2f}".format(idx+1, *notas_alum))
else:
    # Este 'else' se ejecuta cuando el 'for' termina
    print("-------------------------------------------------")
    print("           {:5.2f} {:5.2f} {:5.2f} {:5.2f} {:5.2f}".format(*prom_evaluaciones))
    
# (El número de aprobados se calcula pero no se imprime en este bloque,
# se usa en el bloque siguiente de colorama)


# ==================================
# %% BONUS TRACK 2: Imprimir con Colores
# ==================================
#
# Esta es la misma solución, pero usando la librería `colorama`
# para pintar de rojo los desaprobados.
#
# ¡Necesitas instalarla! -> pip install colorama
# ---

print("\n--- Solución Ejemplo Notas (¡con Colores!) ---")

try:
    # Intentamos importar colorama
    from colorama import Fore, Style, Back
    
    # ¡OJO! Este código es ligeramente diferente al anterior
    # (recalcula todo)
    
    notas = np.random.randint(5, 19, (15, 5))
    prom_alumno = np.mean(notas, axis=1) # Este es 1D (15,)
    prom_evaluacion = np.mean(notas, axis=0)
    num_aprob = prom_alumno[prom_alumno > 10.5].size # Ojo: > 10.5
    
    print("ALUMNO        N1    N2    N3    N4    N5    PROM")
    print("=================================================")
    
    # `zip` junta las filas de notas (de `notas`)
    # con los promedios (de `prom_alumno`)
    for idx, (notas_alum, promedio) in enumerate(zip(notas, prom_alumno)):
        print(Fore.MAGENTA, end='') # Color para el "Alumno X"
        print("Alumno {:2}: ".format(idx+1), end='')
        
        # Iteramos sobre las 5 notas de ESE alumno
        for nota in notas_alum:
            if nota < 10.5:
                print(Fore.RED, end='')
            else:
                print(Fore.BLUE, end='')
            print("{:5.0f} ".format(nota), end='')
        else:
            # Este 'else' es del 'for nota...'
            # Se ejecuta después de imprimir las 5 notas
            if promedio < 10.5:
                print(Fore.RED, end='')
            else:
                print(Fore.BLUE, end='')
            print("   {:5.2f}".format(promedio)) # Imprime el promedio y un salto de línea
    
    # Reseteamos el color
    print(Style.RESET_ALL, end='')
    print("-------------------------------------------------")
    print("           ", end='')
    
    # Imprimimos los promedios de las evaluaciones
    for nota in prom_evaluacion:
        if nota < 10.5:
            print(Fore.RED, end='')
        else:
            print(Fore.BLUE, end='')
        print("{:5.2f} ".format(nota), end='')
    else:
        print() # Salto de línea al final
    
    print(Style.RESET_ALL) # Reseteo final
    print("Numero de aprobados en el curso: {}/{}".format(num_aprob, prom_alumno.size))

except ImportError:
    # Si 'colorama' no está instalado, avisamos
    print("\n¡Oops! No tienes 'colorama'.")
    print("El reporte con colores no se puede mostrar.")
    print("Instálala con: pip install colorama")