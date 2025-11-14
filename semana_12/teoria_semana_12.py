# -*- coding: utf-8 -*-
# %%
# ##################################################
# ##          Matplotlib: ¡A Graficar!            ##
# ##################################################
#
# Autor: Luis A. Muñoz - 2024
# (Archivo original: Semana_12 - Matplotlib.ipynb)
#
# ¡Bienvenido a Matplotlib! Esta es la librería "clásica" y más
# famosa de Python para crear gráficos. Es la navaja suiza
# para visualizar tus datos, ya sea que vengan de listas
# o, más comúnmente, de arrays de NumPy.
#
# Suena complicado, pero la idea es simple: tienes datos, quieres un dibujo.
#
# Tiene una parte llamada 'pylab' que se diseñó para que la gente
# que venía de MATLAB se sintiera como en casa. Nosotros usaremos
# 'pyplot', que es la forma moderna de hacerlo.
#
# ### Resumen de Comandos Clave (tu "chuleta" o "cheat sheet"):
#
#     plt.plot(data_x, data_y, ...)  # Dibuja el gráfico principal (líneas, puntos).
#     plt.title(str)                # Pone un título general al gráfico.
#     plt.xlabel(str)               # Pone etiqueta al eje X (horizontal).
#     plt.ylabel(str)               # Pone etiqueta al eje Y (vertical).
#     plt.grid(True | False)        # Muestra (o esconde) la cuadrícula (rejilla).
#     plt.legend(list[str1, ...])   # Añade una leyenda (para saber qué es cada línea).
#     plt.tight_layout()            # Ajusta todo para que no se superpongan los títulos.
#     plt.subplots(nf, nc, pos)     # Para crear múltiples gráficos (subgráficas).
#     plt.show()                    # ¡Muestra el gráfico! (Súper importante en scripts .py).
#     plt.figure(figsize=(ancho, alto)) # Define el tamaño del "lienzo" (la figura).
#

# %%
# ##################################################
# ##                Configuración Inicial         ##
# ##################################################
#
# Para usar Matplotlib, no importamos *todo* el paquete.
# Generalmente, solo necesitamos la parte de `pyplot`.
#
# Por convención (¡todo el mundo lo hace así!), lo importamos
# con el alias `plt`. Así, en lugar de escribir `matplotlib.pyplot.plot()`,
# solo escribimos `plt.plot()`. Más fácil, ¿no?

# La línea mágica `%matplotlib inline` era necesaria en versiones
# viejas de Jupyter para que los gráficos aparecieran *dentro*
# del notebook y no en una ventana nueva.
#
# Hoy en día, en Jupyter, VS Code, etc., esto suele ser el
# comportamiento por defecto. En un script .py puro, esta línea
# no tiene efecto, pero es bueno saber qué hacía.
# %matplotlib inline

import matplotlib.pyplot as plt
import numpy as np  # Matplotlib y NumPy son mejores amigos, importémoslo ya.

# %%
# ##################################################
# ##          Tu Primer Gráfico: `plt.plot()`     ##
# ##################################################
#
# `plot` es el caballo de batalla de Matplotlib.
#
# Si le das *una sola lista* de números, `plot` es listo:
# asume que esos son los valores del eje Y (la altura).
# ¿Y el eje X? Simplemente usa los índices de la lista (0, 1, 2, 3...).

# Graficando los datos de una lista/arreglo contra su indice
# Es decir, X = [0, 1, 2, 3, 4, 5]
#          Y = [5, 10, 6, 14, 12, 8]
plt.plot([5, 10, 6, 14, 12, 8])

# --- Un buen gráfico necesita contexto ---
# Un gráfico sin etiquetas es un dibujo inútil.
plt.title("Ventas anuales de Odontologia Pesquera")  # Título
plt.xlabel("Años (implícitos, desde el 0)")         # Etiqueta X
plt.ylabel("Ventas [millones]")                      # Etiqueta Y
plt.grid()  # (Opcional) Ponemos una cuadrícula, ¡ayuda mucho!

# ¡El comando final para mostrar la ventana del gráfico!
# En un script .py, esto es OBLIGATORIO para que el gráfico aparezca.
# En Jupyter a veces no es necesario, pero es buena práctica ponerlo.
plt.show()

# %%
# --- Personalizando el Gráfico (Keywords) ---
#
# El gráfico anterior se ve... simple. Podemos mejorarlo.
# El método `plot` acepta un montón de argumentos "keyword" (palabras clave)
# para cambiar el "look".

# Personalizar un grafico con argumentos explícitos
plt.plot([5, 10, 6, 14, 12, 8],
         linewidth=3,           # Grosor de la línea
         marker='o',            # Marcador (un círculo 'o')
         markersize=12,         # Tamaño del marcador
         markerfacecolor='red', # Color de relleno del marcador
         markeredgecolor='black', # Color del borde del marcador
         color='green',         # Color de la línea
         linestyle='dashed')    # Estilo de la línea (punteada)

plt.title("Ventas anuales de Odontologia Pesquera")
plt.xlabel("Años")
plt.ylabel("Ventas [millones]")
plt.grid()
plt.show()

# %%
# --- Personalizando el Gráfico (Estilo MATLAB) ---
#
# Escribir todo eso es un poco largo.
# Hay un "atajo" estilo MATLAB: una cadena de texto corta que
# combina [color][marcador][línea].
# Es más rápido de escribir, pero menos legible.

# Personalizar un grafico con el atajo
# '-ms' significa:
#   - : línea sólida
#   m : color magenta
#   s : marcador cuadrado (square)
# (El orden no importa tanto, 'ms-' también funciona)
plt.plot([5, 10, 6, 14, 12, 8], '-ms')
plt.title("Ventas anuales de Odontologia Pesquera")
plt.xlabel("Años")
plt.ylabel("Ventas [millones]")
plt.grid()
plt.show()

# %%
# --- Dando valores a X e Y ---
#
# ¿Qué pasa si le damos *dos* listas a `plot`?
# `plot(lista_x, lista_y)`
#
# Matplotlib las empareja automáticamente:
# (x[0], y[0]), (x[1], y[1]), (x[2], y[2]), ...

# Graficar con datos explícitos para X e Y
anios = [2014, 2015, 2016, 2017, 2018, 2019]
ventas = [5, 10, 6, 14, 12, 8]

# '-bo' significa:
#   - : línea sólida (se puede omitir si pones marcador)
#   b : color azul (blue)
#   o : marcador circular
plt.plot(anios, ventas, '-bo')

plt.title("Ventas anuales de Odontologia Pesquera")
plt.xlabel("Años")
plt.ylabel("Ventas [millones]")
plt.grid()
plt.show()

# %%
# ##################################################
# ##         Graficando Funciones (con NumPy)     ##
# ##################################################
#
# Aquí es donde Matplotlib brilla junto a NumPy.
# Vamos a graficar una onda senoidal:
#
#   y = A * sin(2 * pi * f * t)
#
# Donde:
#   A = Amplitud (qué tan alta es la onda)
#   f = Frecuencia (cuántos ciclos por segundo, o Hertz)
#   t = Tiempo (nuestro eje X)
#
# Para esto, necesitamos crear un "vector" (un array) de tiempo.
# Usaremos `np.linspace` para crear un rango de números suaves.

A, f = 1, 1  # Amplitud = 1, Frecuencia = 1 Hz

# Creamos 50 puntos (por defecto) entre 0 y 1 segundo
# 50 puntos es poco, pero para 1Hz es suficiente.
t = np.linspace(0, 1)
y = A * np.sin(2 * np.pi * f * t)

plt.plot(t, y)
plt.title("Señal Senoidal (1 Hz)")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# %%
# --- El Problema del "Aliasing" (Muestreo incorrecto) ---
#
# ¿Qué pasa si aumentamos la frecuencia a 12 Hz pero mantenemos
# los mismos 50 puntos para *todo* el segundo?
#
#   A, f = 1, 12
#   t = np.linspace(0, 1)  <-- ¡Solo 50 puntos!
#
# El resultado se verá horrible. No es una senoide, es un desastre.
#
# Esto se llama "aliasing". Es como si quisieras tomar una foto
# de un auto de carreras con una cámara que tarda 1 segundo por foto.
# No vas a capturar el movimiento real. Verás un manchón borroso.
#
# **Solución:** Necesitamos *más muestras* (más puntos en `t`)
# si la señal es *más rápida* (mayor frecuencia).
#
# Vamos a ajustar el código para que siempre haya 50 puntos *por ciclo*.

A, f = 1, 12  # Frecuencia = 12 Hz

# Queremos 50 puntos *por periodo* (por ciclo).
# Como hay 'f' ciclos (12), necesitamos 12 * 50 puntos en total.
# np.linspace(inicio, fin, numero_de_puntos)
t = np.linspace(0, 1, 50 * f)

y = A * np.sin(2 * np.pi * f * t)

plt.plot(t, y)
plt.title("Señal Senoidal (12 Hz - bien muestreada)")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# ¡Moraleja! El "eje x" (tu vector de tiempo o datos)
# es tan importante como el "eje y".

# %%
# ##################################################
# ##      Varias Gráficas en una Sola Figura      ##
# ##################################################
#
# ¿Y si quiero comparar dos gráficos? Puedes "superponerlos".
#
# --- Método 1: Todo en una llamada a `plot` ---
# Le pasas más pares (x, y, formato) a `plot`:
#   plt.plot(x1, y1, x2, y2, ...)

A, f = 1, 5
t = np.linspace(0, 1, 50 * f)
y1 = A * np.sin(2 * np.pi * f * t)
y2 = A / 3 * np.cos(2 * np.pi * 2 * f * t)  # Otra señal (doble frec, 1/3 amp)

# Pasamos (t, y1) y luego (t, y2) en una sola llamada
plt.plot(t, y1, t, y2)

plt.title("Señales trigonometricas")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Amplitud")

# ¡IMPORTANTE! Si tienes más de un gráfico, necesitas una leyenda
# para que la gente sepa qué es qué.
plt.legend(['seno', 'coseno'])

plt.grid()
plt.show()

# %%
# --- Método 2: Múltiples llamadas a `plot` ---
#
# Esta forma es (en mi opinión) más ordenada.
# Puedes llamar a `plt.plot` varias veces.
#
# Matplotlib "acumula" los gráficos en la misma figura
# (como si pusieras capas en Photoshop)
# hasta que finalmente llamas a `plt.show()`.

A, f = 1, 5
t = np.linspace(0, 1, 50 * f)
y1 = A * np.sin(2 * np.pi * f * t)
y2 = A / 3 * np.cos(2 * np.pi * 2 * f * t)

# 1. Dibuja el primer gráfico (rojo)
plt.plot(t, y1, 'r')

# 2. Dibuja el segundo gráfico (verde, guión-punto)
plt.plot(t, y2, '-.g')

plt.title("Señales trigonometricas (Método 2)")
plt.xlabel("Tiempo [seg]")
plt.ylabel("Amplitud")
plt.legend(['seno', 'coseno'])
plt.grid()

# 3. Muestra todo lo acumulado
plt.show()


# %%
# ##################################################
# ##                Sub-Gráficas (Subplots)       ##
# ##################################################
#
# A veces no quieres superponer los gráficos, sino ponerlos
# uno al lado del otro, o uno encima del otro, en una "parrilla".
#
# Para esto, usamos `plt.subplot()`.
#
# Funciona con un código de 3 números: (filas, columnas, índice)
#
#   `plt.subplot(211)` significa:
#     - 2 filas
#     - 1 columna
#     - 1: activa el *primer* gráfico (el de arriba).
#
#   `plt.subplot(212)` significa:
#     - 2 filas
#     - 1 columna
#     - 2: activa el *segundo* gráfico (el de abajo).
#
# Después de llamar a `subplot`, todos los comandos (plot, title, etc.)
# se aplican SOLO a ese "eje" activo.
#
# **Pro-Tip:** Usa `plt.tight_layout()` antes de `plt.show()`
# para que los títulos y etiquetas no se choquen entre sí.


# --- Ejemplo 4x1 (4 filas, 1 columna) ---

A, f = 1, 5
t = np.linspace(0, 1, 50 * f)
y1 = A * np.sin(2 * np.pi * f * t)
y2 = A * np.cos(2 * np.pi * 2 * f * t) * np.exp(-2.6 * t)
y3 = 2 * np.pi * np.exp(-t) * np.sin(2 * np.pi * t) - np.exp(t) * np.cos(2 * np.pi * t)
y4 = np.sin(t) * np.cos(1 / (t + 0.1))

# Especificamos el tamaño de la Figura (lienzo) total
# (ancho, alto) en pulgadas
fig = plt.figure(figsize=(6, 8))

# ---- Gráfico 1 (4 filas, 1 columna, pos 1) ----
plt.subplot(411)
plt.plot(t, y1)
plt.title("Funcion 1")

# ---- Gráfico 2 (4 filas, 1 columna, pos 2) ----
plt.subplot(412)
plt.plot(t, y2)
plt.title("Funcion 2")

# ---- Gráfico 3 (4 filas, 1 columna, pos 3) ----
plt.subplot(413)
plt.plot(t, y3)
plt.title("Funcion 3")

# ---- Gráfico 4 (4 filas, 1 columna, pos 4) ----
plt.subplot(414)
plt.plot(t, y4)
plt.title("Funcion 4")

# Ajusta automáticamente el espaciado para evitar superposiciones
plt.tight_layout()
plt.show()

# %%
# --- Ejemplo 1x2 (1 fila, 2 columnas) ---

A, f = 1, 5
t = np.linspace(0, 1, 50 * f)
y1 = A * np.sin(2 * np.pi * f * t)
y2 = A * np.cos(2 * np.pi * 2 * f * t) * np.exp(-2.6 * t)

fig = plt.figure(figsize=(8, 3))

# ---- Gráfico 1 (1 fila, 2 columnas, pos 1) ----
plt.subplot(121)
plt.plot(t, y1)
plt.title("Funcion 1")

# ---- Gráfico 2 (1 fila, 2 columnas, pos 2) ----
plt.subplot(122)
plt.plot(t, y2)
plt.title("Funcion 2")

plt.tight_layout()
plt.show()

# %%
# --- Ejemplo 2x2 (2 filas, 2 columnas) ---

A, f = 1, 5
t = np.linspace(0, 1, 50 * f)
y1 = A * np.sin(2 * np.pi * f * t)
y2 = A * np.cos(2 * np.pi * 2 * f * t) * np.exp(-2.6 * t)
y3 = 2 * np.pi * np.exp(-t) * np.sin(2 * np.pi * t) - np.exp(t) * np.cos(2 * np.pi * t)
y4 = np.sin(t) * np.cos(1 / (t + 0.1))

fig = plt.figure(figsize=(10, 6))

# ---- Gráfico 1 (2 filas, 2 columnas, pos 1) ----
plt.subplot(221)
plt.plot(t, y1)
plt.title("Funcion 1")

# ---- Gráfico 2 (2 filas, 2 columnas, pos 2) ----
plt.subplot(222)
plt.plot(t, y2)
plt.title("Funcion 2")

# ---- Gráfico 3 (2 filas, 2 columnas, pos 3) ----
plt.subplot(223)
plt.plot(t, y3)
plt.title("Funcion 3")

# ---- Gráfico 4 (2 filas, 2 columnas, pos 4) ----
plt.subplot(224)
plt.plot(t, y4)
plt.grid()
plt.title("Funcion 4")

plt.tight_layout()
plt.show()

# %%
# --- Ejemplo de Grilla Mixta (¡se puede!) ---
# Puedes mezclar las definiciones de subplot

A, f = 1, 5
t = np.linspace(0, 1, 50 * f)
y1 = A * np.sin(2 * np.pi * f * t)
y2 = A * np.cos(2 * np.pi * 2 * f * t) * np.exp(-2.6 * t)
y3 = 2 * np.pi * np.exp(-t) * np.sin(2 * np.pi * t) - np.exp(t) * np.cos(2 * np.pi * t)

fig = plt.figure(figsize=(8, 6))

# --- Fila Superior ---
# 2 filas, 2 columnas, pos 1
plt.subplot(221)
plt.plot(t, y1)
plt.title("Funcion 1")

# 2 filas, 2 columnas, pos 2
plt.subplot(222)
plt.plot(t, y2)
plt.title("Funcion 2")

# --- Fila Inferior (que ocupa todo el ancho) ---
# 2 filas, 1 columna, pos 2
# (Piensa que la figura se divide en 2 filas (21x). La fila 1
# la dividimos en 2 (221, 222). La fila 2 la dejamos entera (212)).
plt.subplot(212)
plt.plot(t, y3)
plt.title("Funcion 3")
plt.grid()

plt.tight_layout()
plt.show()

# %%
# ##################################################
# ##              Otros Tipos de Gráficos         ##
# ##################################################
#
# Matplotlib no solo vive de `plot`. Aquí un vistazo rápido
# a otros tipos de gráficos muy comunes.

# --- Gráfico con ejes logarítmicos ---
# Muy útil cuando tus datos cubren varios órdenes de magnitud
# (ej: de 1 a 10,000,000). Comprime los números grandes.

x = np.linspace(0.1, 60, 1000)
y = 2 ** (-0.2 * x + 10)

plt.figure(figsize=(10, 6))

# Eje normal (Lineal)
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.grid()
plt.title("Lineal-Lineal")

# Eje X logarítmico
plt.subplot(2, 2, 2)
plt.semilogx(x, y)
plt.grid()
plt.title("semilogx (X es log)")

# Eje Y logarítmico
plt.subplot(2, 2, 3)
plt.semilogy(x, y)
plt.grid()
plt.title("semilogy (Y es log)")

# Ambos ejes logarítmicos
plt.subplot(2, 2, 4)
plt.loglog(x, y)
plt.grid()
plt.title("loglog (Ambos log)")

plt.tight_layout()
plt.show()

# %%
# --- Grafico de barras (`plt.bar`) ---
# Perfecto para categorías.

ventas = np.array([10, 15, 16, 23, 18, 12, 19, 12, 17, 20, 19, 24])
mes = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
       'Jul', 'Ago', 'Set', 'Oct', 'Nov', 'Dic']

plt.figure(figsize=(10, 5)) # Hacemos la figura más ancha
plt.bar(mes, ventas)
# También existe horizontal: plt.barh(mes, ventas)

plt.title("Ventas anuales")
plt.xlabel("Meses")
plt.ylabel("Ventas [millones]")

# Rota las etiquetas del eje X para que no se amontonen
plt.xticks(rotation=45)

plt.show()

# %%
# --- Graficos polares (`plt.polar`) ---
# En vez de (x, y), usamos (ángulo, radio).
# Ideal para cosas que dependen de una dirección.

ang = np.linspace(0, 2 * np.pi, 200)  # 0 a 360 grados
rad = 3 * np.cos(0.5 * ang)**2 + np.sin(4 * ang)

plt.polar(ang, rad)
plt.show()

# %%
# --- Grafico de torta (`plt.pie`) ---
# Útil para mostrar proporciones (porcentajes).

notas = [11, 7, 8, 7, 15, 18, 3, 11, 12]

# 1. Procesamos los datos: contamos cuántos hay en cada rango
mal = len(list(filter(lambda x: x <= 8, notas)))
regular = len(list(filter(lambda x: (x > 8) & (x <= 12), notas)))
bien = len(list(filter(lambda x: x > 12, notas)))

dist_notas = [mal, regular, bien]

# 2. Configuramos el gráfico
colors = ['red', 'yellow', 'green']
# "Explode" saca una porción de la torta
explode = [0.1, 0, 0]  # Saca la primera porción (roja) 10%

# 3. Graficamos
# autopct muestra el porcentaje dentro de la torta
plt.pie(dist_notas, autopct="%1.1f%%", colors=colors,
        explode=explode, shadow=True)

plt.title("Distribucion de notas de la PC")
plt.legend(["Mal (0 - 8)", "Regular (9 - 12)", "Bien (13 - 20)"], loc='lower left')
plt.show()


# %%
# ##################################################
# ##      Ejemplo de Aplicación: POO + Matplotlib ##
# ##################################################
#
# Vamos a usar Matplotlib para *visualizar* un objeto
# que creemos con Programación Orientada a Objetos.
#
# La idea es que el *propio objeto* sepa cómo dibujarse.

class Circulo:
    """
    Esta clase define un Círculo con un radio y un centro.
    """
    def __init__(self, radio=1, centro=(0, 0)):
        self.radio = radio
        self.centro = centro
        print(f"Círculo creado: radio={self.radio}, centro={self.centro}")

    def area(self):
        """Calcula el área del círculo."""
        return np.pi * self.radio**2

    def cart2polar(self):
        """
        Genera los puntos (x, y) del borde del círculo
        para poder graficarlos con `plt.plot`.
        Devuelve dos arrays: x, y
        """
        # Creamos un montón de ángulos (de 0 a 2*pi)
        ang = np.arange(0, 2 * np.pi, 0.01)
        # Calculamos x e y y los desplazamos al centro
        x = self.radio * np.cos(ang) + self.centro[0]
        y = self.radio * np.sin(ang) + self.centro[1]
        return x, y

    def __repr__(self):
        """Representación 'oficial' del objeto."""
        return "Circulo(radio={}, centro={})".format(self.radio, self.centro)

# %%
# --- Prueba 1: Círculos aleatorios ---

# Generamos 5 radios y 5 centros aleatorios
radios = np.random.randint(5, 20, (5,))      # 5 radios entre 5 y 19
centros = np.random.randint(0, 12, (5, 2))   # 5 pares (x,y) entre 0 y 11

# Creamos una lista de nuestros objetos Circulo usando "list comprehension"
lista_circulos = [Circulo(radios[i], (centros[i, 0], centros[i, 1])) for i in range(5)]

print("\n--- Lista de Círculos Creados ---")
print(lista_circulos)

# %%
# --- Graficando los objetos ---
# Ahora, recorremos la lista de objetos y le pedimos a cada uno
# que nos dé sus puntos (x,y) para graficarlos.

fig = plt.figure(figsize=(12, 8))

for circ in lista_circulos:
    x, y = circ.cart2polar()  # El objeto sabe cómo calcular sus puntos
    # Graficamos y ponemos su área en la leyenda
    plt.plot(x, y, label='Area: {:.2f}'.format(circ.area()))

plt.legend()  # Mostramos la leyenda con las áreas
# 'axis('square')' es CLAVE para que los círculos no parezcan óvalos
# Asegura que la escala de X e Y sea la misma.
plt.axis('square')
plt.title("Visualización de Objetos Círculo")
plt.show()

# %%
# --- Prueba 2: Círculos concéntricos ---

# Creamos círculos con radios del 1 al 15, todos en (0,0)
for circ in [Circulo(r) for r in range(1, 16)]:
    x, y = circ.cart2polar()
    plt.plot(x, y)

plt.axis('square')
plt.title("Circulos concentricos")
plt.show()


# %%
# ##################################################
# ##      Ejemplo de Aplicación: Simulación (Dados) ##
# ##################################################
#
# Vamos a simular el lanzamiento de 'n' dados 'm' veces y mostrar
# la distribución de probabilidad (el histograma) de los resultados.
# ¿Es más probable sacar 7 o 12 con dos dados? ¡Veámoslo!

print("--- Simulación de Dados ---")
# En un script .py, podemos pedir los datos al usuario:
# n_dados = int(input("Ingrese el numero de dados: "))
# n_veces = int(input("Ingrese el numero de veces: "))

# Para que el script sea rápido, usemos valores fijos:
n_dados = 2      # Simular 2 dados
n_veces = 100000  # 100,000 lanzamientos (¡muchos!)

print(f"Simulando {n_dados} dados, {n_veces} veces...")

# --- Simulación ---
# Creamos una matriz (n_dados x n_veces) con números aleatorios del 1 al 6
# Es como tener 'n_veces' columnas, y cada columna es un lanzamiento de 'n_dados'
dados = np.random.randint(1, 7, (n_dados, n_veces))

# Sumamos los dados para cada lanzamiento (sumamos las columnas, axis=0)
# El resultado es un array de 'n_veces' elementos (ej: [7, 5, 12, 9, ...])
result = np.sum(dados, axis=0)

# --- Cálculo de Probabilidad ---
prob = np.array([])  # un array vacío

# El resultado mínimo es (n_dados * 1) -> ej: 2 dados, min=2 (1+1)
# El resultado máximo es (n_dados * 6) -> ej: 2 dados, max=12 (6+6)
# El +1 es porque range() excluye el último número.
rango_resultados = np.arange(n_dados, 6 * n_dados + 1)

for n in rango_resultados:
    # Contamos cuántas veces salió el número 'n'
    veces_que_salio_n = result[result == n].size
    # Calculamos la probabilidad (veces / total)
    p = veces_que_salio_n / n_veces
    # Lo añadimos a nuestro array de probabilidades
    prob = np.append(prob, p)

# --- Gráfico ---
plt.bar(rango_resultados, prob) # Gráfico de barras
plt.title("Distribucion del lanzamiento de {} dados ({} veces)".format(n_dados, n_veces))
plt.xlabel("Suma de los dados")
plt.ylabel("Probabilidad")
# Ajustamos los "ticks" del eje X para que muestre todos los números
plt.xticks(rango_resultados)
plt.grid(axis='y') # Ponemos grilla solo en el eje Y
plt.show()

# ¡Deberías ver la famosa "campana" de Gauss!
# Con 2 dados, el 7 es el más probable.

# %%
# ##################################################
# ##      ipywidgets: Interactividad (SOLO JUPYTER) ##
# ##################################################
#
# AVISO IMPORTANTE:
# El siguiente código está diseñado para funcionar *EXCLUSIVAMENTE*
# dentro de un entorno Jupyter (Notebook, Lab) o un IDE
# compatible (como VS Code con soporte para Jupyter).
#
# NO funcionará si ejecutas este archivo .py desde la terminal
# (ej: `python mi_script.py`).
#
# Los "widgets" son controles gráficos (sliders, botones, menús)
# que te permiten cambiar parámetros de tu código en tiempo real
# sin tener que volver a escribir la celda.
#
# He comentado el código para que este script .py pueda
# ejecutarse sin errores, pero te dejo la lógica exacta.

# %%

# En caso de que no estén instalados (en tu entorno de Jupyter):
# !pip install ipywidgets==8.0.1
print("\n--- Sección de ipywidgets (Solo para Jupyter) ---")

# %%
# --- Ejemplo Básico de Widget (Solo en Jupyter) ---
#
# from ipywidgets import IntSlider
#
# Si ejecutas esto en Jupyter, verás un slider
# IntSlider()

# %%
# Para *usar* el valor del widget, necesitas 'display'

# from IPython.display import display
#
# print("Mostrando un IntSlider (solo visible en Jupyter):")
# val = IntSlider()
# display(val)

# %%
# Y en otra celda de Jupyter, podrías leer su valor actual:

# print("El valor actual del slider es (solo en Jupyter):")
# print(val.value)

# %%
# ##################################################
# ##     La magia de `interact` (Solo en Jupyter)   ##
# ##################################################
#
# `interact` es la forma más fácil de usar widgets.
# Creas una función, y `interact` crea los widgets
# *automáticamente* basándose en los argumentos de la función:
#
# * tupla (min, max) o (min, max, step) -> Slider (Int o Float)
# * lista de strings o tuplas -> Menú desplegable
# * Booleano (True/False) -> Checkbox

# --- Ejemplo de `interact` (Solo en Jupyter) ---

# from ipywidgets import interact
# (las otras librerías ya deberían estar importadas)

# 1. Definimos la función que hace el gráfico
#    Toma como parámetros las cosas que queremos controlar
# def circulo_interactivo(r, c, g):
#     """
#     Esta función dibuja un círculo.
#     r = radio
#     c = color
#     g = grilla (grid)
#     """
#     ang = np.linspace(0, 2 * np.pi, 100)
#     x = r * np.cos(ang)
#     y = r * np.sin(ang)
#
#     plt.figure(figsize=(8, 6))
#     plt.plot(x, y, color=c)
#     plt.axis('square')
#     plt.axis([-10, 10, -10 , 10]) # Ejes fijos para ver el cambio de radio
#     plt.grid(g)
#     plt.show() # Importante mostrarlo dentro de la función

# 2. Conectamos la función a `interact`
#    `interact` llamará a `circulo_interactivo` CADA VEZ que muevas un control.

# r=(0, 10) -> Slider de entero de 0 a 10
# c=[('azul', 'blue'), ...] -> Menú desplegable
# g=True -> Checkbox

# print("Creando gráfico interactivo (solo visible en Jupyter):")
# interact(circulo_interactivo,
#          r=(0, 10),  # Slider de Radio
#          c=[('Azul', 'blue'), ('Rojo', 'red'), ('Verde', 'green')], # Menú de Color
#          g=True)     # Checkbox de Grilla

# %%
# --- `interact` como decorador (Solo en Jupyter) ---
#
# Es exactamente lo mismo que antes, pero se escribe encima de la función
# usando el `@`. Es un estilo más "Pythonico" y ordenado.

# @interact(r=(0, 10), c=[('Azul', 'blue'), ('Rojo', 'red'), ('Verde', 'green')], g=True)
# def circulo_decorado(r, c, g):
#     ang = np.linspace(0, 2 * np.pi, 100)
#     x = r * np.cos(ang)
#     y = r * np.sin(ang)
#
#     plt.figure(figsize=(8, 6))
#     plt.plot(x, y, color=c)
#     plt.axis('square')
#     plt.axis([-10, 10, -10 , 10])
#     plt.grid(g)
#     plt.show()


# %%
# Para más información (si estás en Jupyter):
# - Lista de widgets: https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
# - Uso de interact: https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html

print("\nFin del script de Matplotlib.")