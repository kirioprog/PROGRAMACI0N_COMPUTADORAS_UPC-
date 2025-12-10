# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *

# ==============================================================================
# TEMA: TKINTER - GUI EN PYTHON (DISEÑO)
# ==============================================================================
# Autor: Luis A. Muñoz - 2024
# Adaptado por: Tu Asistente de IA (PROGRAMACION)
#
# IDEAS CLAVE:
# 1. Tkinter es la librería nativa para interfaces gráficas (GUI).
# 2. El diseño necesita un "wireframe" (un plan, un dibujo en servilleta).
# 3. La magia está en los FRAMES (marcos) para distribuir secciones.
# 4. Los WIDGETS (botones, etiquetas) se colocan dentro de los frames.
# ==============================================================================

print("--- INICIANDO CURSO DE TKINTER ---")
print("NOTA IMPORTANTE: Tkinter detiene el código mientras la ventana está abierta.")
print(">>> CIERRA CADA VENTANA QUE APAREZCA PARA QUE SE EJECUTE EL SIGUIENTE BLOQUE DE CÓDIGO <<<\n")

# ==============================================================================
# 1. CÓDIGO BASE: EL "HOLA MUNDO" DE LAS VENTANAS
# ==============================================================================
# Aquí creamos la raíz (root). Imagina que 'root' es el tronco del árbol.
# 'mainloop()' es el hechizo que mantiene la ventana viva y escuchando clics.

print("Ejecutando ejemplo 1: Ventana vacía básica...")
root = Tk()
root.mainloop() 
print("-> Ventana 1 cerrada.\n")


# ==============================================================================
# 2. PROPIEDADES DE LA VENTANA (TUNEANDO LA APP)
# ==============================================================================
# Vamos a darle personalidad. Título, tamaño fijo y color de fondo.
# geometry("ancho x alto + x_pantalla + y_pantalla")

print("Ejecutando ejemplo 2: Ventana configurada (gris)...")
root = Tk()
root.title("Tkinter App")
root.resizable(0, 0) # (0,0) significa: No redimensionable ni en ancho ni en alto.
root.geometry("400x300+100+100")
root.config(bg='gray') # bg = background

root.mainloop()
print("-> Ventana 2 cerrada.\n")


# ==============================================================================
# 3. AÑADIENDO UN LABEL (ETIQUETA)
# ==============================================================================
# Los widgets (como Label) se crean en dos pasos:
# 1. Se definen (quién es su padre, texto, fuente, colores).
# 2. Se "empaquetan" o colocan en la interfaz (aquí usamos .pack()).

print("Ejecutando ejemplo 3: Ventana con Label...")
root = Tk()
root.title("Tkinter App")
root.resizable(0, 0)
root.geometry("400x300+100+100")
root.config(bg='green')

# Definición del widget
label = Label(root, text="Hola mundo", font="Arial 12 bold", fg='white', bg='blue')
# Colocación del widget
label.pack()

root.mainloop()
print("-> Ventana 3 cerrada.\n")


# ==============================================================================
# 4. AUTO-AJUSTE (GEOMETRÍA DINÁMICA)
# ==============================================================================
# Si quitamos 'root.geometry(...)', la ventana se encoge como ropa lavada con agua caliente
# hasta ajustarse exactamente al tamaño de sus hijos (los widgets).
# Nota: El fondo verde de 'root' casi no se verá porque el Label ocupará todo.

print("Ejecutando ejemplo 4: Ventana auto-ajustada...")
root = Tk()
root.title("Tkinter App")
root.resizable(0, 0)
root.config(bg='green')

label = Label(root, text="Hola mundo", font="Arial 12 bold", fg='white', bg='blue')
label.pack()

root.mainloop()
print("-> Ventana 4 cerrada.\n")


# ==============================================================================
# 5. CATÁLOGO DE WIDGETS COMUNES
# ==============================================================================
# Aquí presentamos al elenco principal de actores:
# - Label: Texto estático.
# - Button: Para hacer clic.
# - Entry: Cajita para escribir texto (input).
# - Checkbutton: Casilla de verificación (sí/no).
# - Radiobutton: Selección única (opción A o B).

print("Ejecutando ejemplo 5: Todos los widgets básicos...")
root = Tk()
root.title("Tkinter App")
root.resizable(0, 0)
root.geometry("400x300+100+100")
root.config(bg='green')

label = Label(root, text="Label", font="Arial 12")
button = Button(root, text="Button", font="Arial 12")
entry = Entry(root, font="Arial 12")
checkbutton = Checkbutton(root, text="Checkbutton", font="Arial 12")
radiobutton = Radiobutton(root, text="Radiobutton", font="Arial 12")

# Usamos pack con 'pady' (padding vertical) para que no estén pegados
label.pack(pady=10)
button.pack(pady=10)
entry.pack(pady=10)
checkbutton.pack(pady=10)
radiobutton.pack(pady=10)

root.mainloop()
print("-> Ventana 5 cerrada.\n")


# ==============================================================================
# 6. GESTORES DE GEOMETRÍA: PACK (BÁSICO)
# ==============================================================================
# pack() es un gestor relativo. Por defecto, apila cosas una debajo de otra (TOP).
# Es flexible pero a veces caprichoso.

print("Ejecutando ejemplo 6: Pack por defecto...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

label1 = Label(root, text="Label 1", font="Arial 20", bg='red')
label2 = Label(root, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(root, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(root, text="Label 4", font="Arial 20", bg='yellow')

label1.pack()
label2.pack()
label3.pack()
label4.pack()

root.mainloop()
print("-> Ventana 6 cerrada.\n")


# ==============================================================================
# 6.1. PACK (SIDE=LEFT)
# ==============================================================================
# Podemos decirle que empaquete hacia la izquierda. Se irán poniendo uno al lado del otro.

print("Ejecutando ejemplo 6.1: Pack hacia la izquierda...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

label1 = Label(root, text="Label 1", font="Arial 20", bg='red')
label2 = Label(root, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(root, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(root, text="Label 4", font="Arial 20", bg='yellow')

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)

root.mainloop()
print("-> Ventana 6.1 cerrada.\n")


# ==============================================================================
# 6.2. PACK (MIXTO - CUIDADO AQUÍ)
# ==============================================================================
# Si mezclas lados (LEFT, TOP, RIGHT), pack empieza a comerse el espacio disponible.
# Label 1 toma la izquierda, lo que queda se usa para Label 2 (arriba), etc.
# Es confuso, por eso generalmente usamos Frames para organizar esto mejor.

print("Ejecutando ejemplo 6.2: Pack mixto (relativo)...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

label1 = Label(root, text="Label 1", font="Arial 20", bg='red')
label2 = Label(root, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(root, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(root, text="Label 4", font="Arial 20", bg='yellow')

label1.pack(side=LEFT)
label2.pack()
label3.pack()
label4.pack(side=RIGHT)

root.mainloop()
print("-> Ventana 6.2 cerrada.\n")


# ==============================================================================
# 6.3. PACK (FILL - LLENAR ESPACIO)
# ==============================================================================
# fill=X: Estírate a lo ancho.
# fill=Y: Estírate a lo alto (necesita que el contenedor tenga altura).

print("Ejecutando ejemplo 6.3: Pack con Fill...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

label1 = Label(root, text="Arriba", font="Arial 20", bg='red')
label2 = Label(root, text="Centro", font="Arial 20", bg='blue')
label3 = Label(root, text="Derecha", font="Arial 20", bg='magenta')

label1.pack()
label2.pack(fill=X)         # Se estira horizontalmente
label3.pack(side=LEFT, fill=Y) # Se estira verticalmente

root.mainloop()
print("-> Ventana 6.3 cerrada.\n")


# ==============================================================================
# 7. GESTORES DE GEOMETRÍA: GRID (LA MATRIZ)
# ==============================================================================
# Grid es como Excel: filas y columnas. Es mucho más preciso para formularios.

print("Ejecutando ejemplo 7: Grid básico...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

label1 = Label(root, text="Label 1", font="Arial 20", bg='red')
label2 = Label(root, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(root, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(root, text="Label 4", font="Arial 20", bg='yellow')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

root.mainloop()
print("-> Ventana 7 cerrada.\n")


# ==============================================================================
# 7.1. GRID (SPAN Y STICKY)
# ==============================================================================
# columnspan/rowspan: Ocupar más de una celda (combinar celdas).
# sticky: "Pegajoso". Hacia dónde se pega el widget dentro de su celda (N, S, E, W).
# W = West (Oeste/Izquierda), E = East (Este/Derecha), etc.

print("Ejecutando ejemplo 7.1: Grid avanzado...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

label1 = Label(root, text="Label 1", font="Arial 20", bg='red')
label2 = Label(root, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(root, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(root, text="Label 4", font="Arial 20", bg='yellow')

# Label 1 ocupa 2 columnas y se pega a la izquierda (W)
label1.grid(row=0, column=0, columnspan=2, sticky=W)
# Label 2 ocupa 2 filas y se pega abajo (S)
label2.grid(row=1, column=0, rowspan=2, sticky=S)
label3.grid(row=1, column=1)
label4.grid(row=2, column=1)

root.mainloop()
print("-> Ventana 7.1 cerrada.\n")


# ==============================================================================
# 8. FRAMES: EL SECRETO DEL DISEÑO
# ==============================================================================
# Los Frames son contenedores invisibles.
# REGLA DE ORO:
# 1. Usa PACK para organizar los FRAMES principales (grandes bloques).
# 2. Usa GRID para organizar los WIDGETS dentro de esos Frames.

print("Ejecutando ejemplo 8: Frames estructurales...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

frm1 = Frame(root)
frm2 = Frame(root)
frm1.pack(side=TOP)
frm2.pack(side=BOTTOM)

# Nota: El padre de estos labels ya no es 'root', sino 'frm1' o 'frm2'.
label1 = Label(frm1, text="Label 1", font="Arial 20", bg='red')
label2 = Label(frm1, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(frm2, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(frm2, text="Label 4", font="Arial 20", bg='yellow')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)

root.mainloop()
print("-> Ventana 8 cerrada.\n")


# ==============================================================================
# 9. PADDING (ESPACIADO)
# ==============================================================================
# El diseño necesita aire. 'padx' y 'pady' crean márgenes.
# Aquí creamos un Frame Principal (frm) que contiene a los otros dos.

print("Ejecutando ejemplo 9: Padding en Frames y Widgets...")
root = Tk()
root.title("Tkinter App")
root.config(bg='green')

# Frame principal que contiene todo
frm = Frame(root)
frm1 = Frame(frm)
frm2 = Frame(frm)

# Padding externo para el frame principal y los sub-frames
frm.pack(padx=10, pady=10)
frm1.pack(padx=10, pady=10)
frm2.pack(padx=10, pady=10)

label1 = Label(frm1, text="Label 1", font="Arial 20", bg='red')
label2 = Label(frm1, text="Label 2", font="Arial 20", bg='blue')
label3 = Label(frm2, text="Label 3", font="Arial 20", bg='magenta')
label4 = Label(frm2, text="Label 4", font="Arial 20", bg='yellow')

# Padding interno para los widgets (separación entre ellos)
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
label3.grid(row=0, column=0, padx=5, pady=5)
label4.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
print("-> Ventana 9 cerrada.\n")


# ==============================================================================
# 10. PROYECTO FINAL: SIGN UP WINDOW
# ==============================================================================
# Vamos a construir una pantalla de registro real.
# Iteración 1: Estructura de 3 columnas (Izquierda, Centro, Derecha).
# Nota: Usamos frames de colores y tamaños fijos para visualizar el layout.

print("Ejecutando Proyecto 1: Estructura base (colores)...")
root = Tk()
root.title("tkinter App")
root.resizable(0, 0)
root.geometry("400x280+100+100")

frm = Frame(root)
frm1 = Frame(frm, bg='gray', width=100, height=300)
frm2 = Frame(frm, bg='gray', width=100, height=300)
frm3 = Frame(frm, bg='gray', width=100, height=300)

frm.pack(padx=10, pady=10)
frm1.pack(side=LEFT, padx=10, pady=10)
frm2.pack(side=LEFT, padx=10, pady=10)
frm3.pack(side=LEFT, padx=10, pady=10)

# Llenando el frm1 (Izquierda)
lblSignUp = Label(frm1, text="Sign Up" , font="Arial 12 bold")
lblLogin = Label(frm1, text="Login:")
lblEmail = Label(frm1, text="Email:")
lblPassword = Label(frm1, text="Password:")
lblConfirm = Label(frm1, text="Confirm:")

lblSignUp.grid(row=0, column=0, padx=5, pady=5, sticky=W)
lblLogin.grid(row=1, column=0, padx=5, pady=5, sticky=E)
lblEmail.grid(row=2, column=0, padx=5, pady=5, sticky=E)
lblPassword.grid(row=3, column=0, padx=5, pady=5, sticky=E)
lblConfirm.grid(row=4, column=0, padx=5, pady=5, sticky=E)

root.mainloop()
print("-> Proyecto 1 cerrado.\n")


# ==============================================================================
# 10.1. PROYECTO - ITERACIÓN 2: REDISEÑO DE ESTRUCTURA
# ==============================================================================
# El diseño anterior fallaba en alineación.
# Nueva estrategia: Un frame arriba (frmUp) para el título y uno abajo (frmDown)
# dividido en columnas para los campos.

print("Ejecutando Proyecto 2: Rediseño Arriba/Abajo...")
root = Tk()
root.title("tkinter App")
root.resizable(0, 0)
root.geometry("400x280+100+100")

frm = Frame(root)
frmUp = Frame(frm, bg='gray')
frmDown = Frame(frm, bg='gray')
# Sub-frames dentro de frmDown
frm1 = Frame(frmDown, bg='gray')
frm2 = Frame(frmDown, bg='gray')
frm3 = Frame(frmDown, bg='gray')

frm.pack(padx=10, pady=10)
frmUp.pack(padx=10, pady=10, fill=X)
frmDown.pack(padx=10, pady=10)
# ANCHOR=N es clave para que los frames internos se alineen arriba y no al centro
frm1.pack(side=LEFT, padx=10, pady=10, anchor=N)
frm2.pack(side=LEFT, padx=10, pady=10, anchor=N)
frm3.pack(side=LEFT, padx=10, pady=10, anchor=N)

# --- frmUp (Título) ---
lblSignUp = Label(frmUp, text="Sign Up" , font="Arial 12 bold")
lblSignUp.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# --- frm1 (Etiquetas) ---
lblLogin = Label(frm1, text="Login:")
lblEmail = Label(frm1, text="Email:")
lblPassword = Label(frm1, text="Password:")
lblConfirm = Label(frm1, text="Confirm:")

lblLogin.grid(row=0, column=0, padx=5, pady=5, sticky=E)
lblEmail.grid(row=1, column=0, padx=5, pady=5, sticky=E)
lblPassword.grid(row=2, column=0, padx=5, pady=5, sticky=E)
lblConfirm.grid(row=3, column=0, padx=5, pady=5, sticky=E)

# --- frm2 (Entradas de texto) ---
entLogin = Entry(frm2, width=30)
entEmail = Entry(frm2, width=30)
entPassword = Entry(frm2, width=30)
entConfirm = Entry(frm2, width=30)
chkRemember = Checkbutton(frm2, text="Remember Me")

entLogin.grid(row=0, column=0, padx=5, pady=5)
entEmail.grid(row=1, column=0, padx=5, pady=5)
entPassword.grid(row=2, column=0, padx=5, pady=5)
entConfirm.grid(row=3, column=0, padx=5, pady=5)
chkRemember.grid(row=4, column=0, padx=5, pady=5, sticky=W)

root.mainloop()
print("-> Proyecto 2 cerrado.\n")


# ==============================================================================
# 10.2. PROYECTO - VERSIÓN FINAL
# ==============================================================================
# Simplificación: En lugar de 3 columnas en frmDown, metemos todo en el Grid de
# frmDown directamente. Así podemos colocar el botón "SignUp" en la columna 2
# y todo queda alineado perfectamente.
# Quitamos los colores de fondo para el look final.

print("Ejecutando Proyecto FINAL: Diseño pulido...")
root = Tk()
root.title("tkinter App")
root.resizable(0, 0)
# Quitamos geometry fija para que se ajuste al contenido

frm = Frame(root)
frmUp = Frame(frm)
frmDown = Frame(frm)

frm.pack(padx=10, pady=10)
# anchor=W pega el título a la izquierda.
frmUp.pack(padx=10, pady=10, anchor=W)
frmDown.pack(padx=10, pady=10, anchor=N)

# --- SECCIÓN SUPERIOR ---
lblSignUp = Label(frmUp, text="Sign Up" , font="Arial 12 bold")
lblSignUp.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# --- SECCIÓN INFERIOR (GRID ÚNICO) ---
# Labels con espacios extra para simular alineación visual rápida
lblLogin = Label(frmDown, text="        Login:")
lblEmail = Label(frmDown, text="        Email:")
lblPassword = Label(frmDown, text="        Password:")
lblConfirm = Label(frmDown, text="         Confirm:")

# Entradas
entLogin = Entry(frmDown, width=30)
entEmail = Entry(frmDown, width=30)
entPassword = Entry(frmDown, width=30)
entConfirm = Entry(frmDown, width=30)

# Checkbox y Botón
chkRemember = Checkbutton(frmDown, text="Remember Me")
btnSignUp = Button(frmDown, text="SignUp", width=12)

# Colocación en la GRILA (Grid)
# Columna 0: Etiquetas
lblLogin.grid(row=0, column=0, padx=5, pady=5, sticky=E)
lblEmail.grid(row=1, column=0, padx=5, pady=5, sticky=E)
lblPassword.grid(row=2, column=0, padx=5, pady=5, sticky=E)
lblConfirm.grid(row=3, column=0, padx=5, pady=5, sticky=E)

# Columna 1: Entradas
entLogin.grid(row=0, column=1, padx=5, pady=5)
entEmail.grid(row=1, column=1, padx=5, pady=5)
entPassword.grid(row=2, column=1, padx=5, pady=5)
entConfirm.grid(row=3, column=1, padx=5, pady=5)
chkRemember.grid(row=4, column=1, pady=5, sticky=W)

# Columna 2: Botón (Colocado en la fila 3, al lado de Confirmar, pero desplazado)
btnSignUp.grid(row=3, column=2, padx=20, pady=5)

root.mainloop()
print("-> FIN DEL TUTORIAL. ¡Buen trabajo!")
