# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# TUTORIAL DE TKINTER - GUI EN PYTHON: OPERACIÓN Y EVENTOS
# Autor Original: Luis A. Muñoz - 2024
# Comentarios y Explicaciones: Tu copiloto de IA (estilo PROGRAMACION)
# ==============================================================================

print("--- INICIO DEL TUTORIAL ---")
print("Nota: Cierra cada ventana emergente para pasar al siguiente ejemplo.\n")

# ==============================================================================
# EJEMPLO 1: EL BOTÓN BÁSICO
# ==============================================================================
print(">> Ejemplo 1: Ventana simple con un botón (sin acción aún).")

root = tk.Tk()
root.resizable(0, 0) # Esto bloquea el redimensionamiento, ventana fija.

# Definimos un botón simple.
# 'pack' es el gestor de geometría más básico: apila cosas.
button = tk.Button(root, text="Haz Click", font="Arial 12")
button.pack(padx=25, pady=25)

root.mainloop() # El bucle infinito que mantiene la ventana viva.


# ==============================================================================
# EJEMPLO 2: ASOCIANDO ACCIONES (COMMAND)
# ==============================================================================
print(">> Ejemplo 2: Botón con acción 'command'. Mira la consola al hacer click.")

root = tk.Tk()
root.resizable(0, 0)

# Primero definimos la función. Python necesita conocerla antes de asignarla.
def print_click():
    print("Click (¡Funcionó!)")

# Aquí está la magia: la propiedad `command`.
# OJO: Pasamos el NOMBRE de la función (print_click), NO la ejecutamos (print_click()).
# Si pones paréntesis, se ejecuta sola al arrancar el programa y no al hacer click.
button = tk.Button(root, text="Haz Click", font="Arial 12", command=print_click)
button.pack(padx=25, pady=25)

root.mainloop()


# ==============================================================================
# EJEMPLO 3: EL TRUCO DE LAMBDA (PASANDO ARGUMENTOS)
# ==============================================================================
print(">> Ejemplo 3: Usando 'lambda' para pasar argumentos a la función.")

root = tk.Tk()
root.resizable(0, 0)

def print_click_con_mensaje(message):
    print(message)

# El problema de 'command' es que no deja pasar argumentos directamente.
# Solución: Usamos 'lambda'. Es como un "Caballo de Troya": una función anónima
# vacía que, cuando se ejecuta, llama a nuestra función real con los parámetros.
button = tk.Button(root, text="Haz Click", font="Arial 12", 
                   command=lambda: print_click_con_mensaje("Click con lambda"))
button.pack(padx=25, pady=25)

root.mainloop()


# ==============================================================================
# EJEMPLO 4: LABELS Y EVENTOS MANUALES (BIND)
# ==============================================================================
print(">> Ejemplo 4: Labels y el método '.bind()'. Haz click sobre el texto.")

root = tk.Tk()
root.resizable(0, 0)

def print_click():
    print("Click en Botón")

# Esta función recibe un parámetro 'event'.
# Cuando usas .bind(), Tkinter envía automáticamente información del evento 
# (coordenadas del mouse, tecla presionada, etc.) en ese objeto.
def print_event(event):
    print("Click en Label detectado en coordenadas x={}, y={}".format(event.x, event.y))
    
button = tk.Button(root, text="Haz Click", font="Arial 12", command=print_click)
button.pack(padx=25, pady=25)

label = tk.Label(root, text="¡Hazme click a mí (Label)!", font="Arial 12")
label.pack(padx=25, pady=25)

# Los Labels NO tienen propiedad 'command' por defecto.
# Así que "cableamos" el evento manualmente.
# "<Button-1>" significa Click Izquierdo del Mouse.
label.bind("<Button-1>", print_event)

root.mainloop()


# ==============================================================================
# EJEMPLO 5: BIND CON LAMBDA (IGNORANDO EL EVENTO)
# ==============================================================================
print(">> Ejemplo 5: Bind con Lambda. Pasando argumentos personalizados.")

root = tk.Tk()
root.resizable(0, 0)

def print_click():
    print("Click")

def print_Label(message):
    print(message)
    
button = tk.Button(root, text="Haz Click", font="Arial 12", command=print_click)
button.pack(padx=25, pady=25)

label = tk.Label(root, text="Soy un label!", font="Arial 12")
label.pack(padx=25, pady=25)

# Aquí usamos 'lambda x:'. ¿Por qué la 'x'?
# Porque .bind() SIEMPRE envía el objeto evento. La 'x' captura ese evento
# (aunque no lo usemos) para que no dé error, y luego ejecutamos nuestra función.
label.bind("<Button-1>", lambda x: print_Label('¡Ouch! Eso dolió.'))

root.mainloop()


# ==============================================================================
# EJEMPLO 6: EVENTOS DE MOUSE (ENTER/LEAVE)
# ==============================================================================
print(">> Ejemplo 6: Detectando cuando el mouse entra o sale del botón.")

root = tk.Tk()
root.resizable(0, 0)

def print_message(message):
    print(message)

button = tk.Button(root, text="Pasa el mouse", font="Arial 12", command=lambda:print_message("Click"))
button.pack(padx=25, pady=25)

# <Enter>: El mouse entró al área del widget.
# <Leave>: El mouse salió del área.
button.bind("<Enter>", lambda x: print_message("--> Entraste al botón"))
button.bind("<Leave>", lambda x: print_message("<-- Saliste del botón"))

label = tk.Label(root, text="Soy un label!", font="Arial 12")
label.pack(padx=25, pady=25)
label.bind("<Button-1>", lambda x: print_message('Ouch!'))

root.mainloop()


# ==============================================================================
# EJEMPLO 7: MODIFICANDO WIDGETS CON .CONFIG()
# ==============================================================================
print(">> Ejemplo 7: Actualizando propiedades dinámicamente con .config().")

n_clicks = 0
root = tk.Tk()
root.resizable(0, 0)

def click_button():
    global n_clicks
    # .config() permite cambiar CUALQUIER propiedad del widget después de creado.
    # Aquí cambiamos el texto del Label.
    label.config(text="Num Clicks: {}".format(n_clicks))
    n_clicks += 1
    
button = tk.Button(root, text="Haz Click para contar", font="Arial 12", command=click_button)
button.pack(padx=25, pady=25)

label = tk.Label(root, text="Num Clicks: 0", font="Arial 12")
label.pack(padx=25, pady=25)

root.mainloop()


# ==============================================================================
# EJEMPLO 8: VARIABLES DE CONTROL (STRINGVAR, INTVAR, ETC.)
# ==============================================================================
print(">> Ejemplo 8: Variables de control para conectar widgets.")

# Aquí montamos una estructura más compleja con Frames.
root = tk.Tk()
root.resizable(0, 0)
root.geometry("360x220+200+200") # Tamaño + posición en pantalla
root.title("Multiplica - Demo Variables")

# --- CONCEPTO CLAVE: CLASES VARIABLE ---
# Tkinter no usa variables normales de Python (a = 5). Usa objetos especiales
# que "vigilan" los cambios. Si cambias el objeto, la interfaz se actualiza sola.
var_num = tk.StringVar()         # Para el Entry (evita el "0" por defecto del IntVar)
var_borrar = tk.BooleanVar()     # Para el Checkbutton (True/False)
var_color = tk.IntVar()          # Para los Radiobuttons (0, 1, 2)

frm = tk.Frame(root)
frm1 = tk.Frame(frm)
frm2 = tk.Frame(frm)
frm3 = tk.Frame(frm)

frm.pack(padx=10, pady=10)
frm1.pack(padx=10, pady=10)
frm2.pack(padx=10, pady=10)
frm3.pack(padx=10, pady=10)

# --- frm1: Entradas ---
lblEntry = tk.Label(frm1, text="Numero:")
# textvariable conecta el Entry con nuestra var_num. Lo que escribas va a var_num.
entNum = tk.Entry(frm1, textvariable=var_num) 
chkBorrar = tk.Checkbutton(frm1, text="Borrar?", variable=var_borrar)

lblEntry.grid(row=0, column=0, padx=5, pady=5)
entNum.grid(row=0, column=1, padx=5, pady=5)
chkBorrar.grid(row=0, column=2, padx=5, pady=5)

# --- frm2: Botones y Radios ---
btnXDos = tk.Button(frm2, text="x2", width=6)
btnXTres = tk.Button(frm2, text="x3", width=6)
btnXCinco = tk.Button(frm2, text="x5", width=6)

# Los Radiobuttons comparten la MISMA variable (var_color).
# Cuando seleccionas uno, var_color toma el 'value' asignado.
rdoNegro = tk.Radiobutton(frm2, text="Negro", variable=var_color, value=0)
rdoRojo = tk.Radiobutton(frm2, text="Rojo", variable=var_color, value=1)
rdoAzul = tk.Radiobutton(frm2, text="Azul", variable=var_color, value=2)

btnXDos.grid(row=0, column=0, padx=5, pady=5)
btnXTres.grid(row=0, column=1, padx=5, pady=5)
btnXCinco.grid(row=0, column=2, padx=5, pady=5)
rdoNegro.grid(row=1, column=0, padx=5, pady=5)
rdoRojo.grid(row=1, column=1, padx=5, pady=5)
rdoAzul.grid(row=1, column=2, padx=5, pady=5)

# --- frm3: Resultado ---
lblResultado = tk.Label(frm3, text="Resultado: {:5}".format(""), font="Arial 10")
lblResultado.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()


# ==============================================================================
# EJEMPLO 9: WIDGETS ADICIONALES (LABELFRAME, TEXT, LISTBOX, SCROLLBAR)
# ==============================================================================

# 9.1 LABELFRAME
print(">> Ejemplo 9.1: LabelFrame (Un marco con título).")
root = tk.Tk()
frm = tk.LabelFrame(root, text=" Datos Personales ") # Marco decorativo
frm.pack(padx=10, pady=10)

lbl = tk.Label(frm, text="Dato: ")
ent = tk.Entry(frm)
lbl.grid(row=0, column=0, padx=5, pady=5)
ent.grid(row=0, column=1, padx=5, pady=5)
root.mainloop()

# 9.2 TEXT (Caja de texto grande)
print(">> Ejemplo 9.2: Text Widget (Para párrafos).")
root = tk.Tk()
frm = tk.Frame()
frm.pack(padx=10, pady=10)
text = tk.Text(frm, width=25, height=12, wrap='word')
text.grid(row=0, column=0, padx=5, pady=5)
root.mainloop()

# 9.3 LISTBOX Y SCROLLBAR
print(">> Ejemplo 9.3: Listbox con Scrollbar funcional.")
root = tk.Tk()
frm = tk.Frame()
frm.pack(padx=10, pady=10)

# Scrollbar: Necesita un comando para saber a quién mover (command=lst_box.yview)
# Listbox: Necesita avisar al scrollbar que se movió (yscrollcommand=yscr.set)
yscr = tk.Scrollbar(frm, orient='vertical')
lst_box = tk.Listbox(frm, width=25, height=6, yscrollcommand=yscr.set)
yscr.config(command=lst_box.yview)

lst_box.pack(side='left')
yscr.pack(side='left', expand=True, fill='y')

# Llenamos la lista
lst_box.delete(0, 'end')
for idx in range(1, 11):
    lst_box.insert('end', f"Opcion {idx}")

# Evento al seleccionar un item de la lista
lst_box.bind("<<ListboxSelect>>", lambda x: print(lst_box.get(lst_box.curselection())))

root.mainloop()


# ==============================================================================
# EJEMPLO 10: LA APP "MULTIPLICA" COMPLETA (Lógica + UI)
# ==============================================================================
print(">> Ejemplo 10: App 'Multiplica' con lógica de negocio completa.")

root = tk.Tk()
root.resizable(0, 0)
root.geometry("360x220+200+200")
root.title("Multiplica - Final")

# Obj-Var
var_num = tk.StringVar()
var_borrar = tk.BooleanVar()
var_color = tk.IntVar()

# Funciones de lógica
def set_color():
    # Diccionario para mapear el valor entero (0,1,2) a nombres de colores en inglés
    colors = {0: 'black', 1: 'red', 2: 'blue'}
    # .get() obtiene el valor del objeto IntVar
    lblResultado.config(fg=colors[var_color.get()])

def print_mult(factor):
    # Uso de try/except para validación: Si el usuario escribe texto, float() falla
    try:
        # IMPORTANTE: .get() para leer, float() para convertir
        result = factor * float(var_num.get())
    except:
        # Si falla la conversión, salimos silenciosamente (o podríamos mostrar error)
        return

    lblResultado.config(text="Resultado: {:10}".format(result))

    # Si el check 'Borrar' está activo, limpiamos el Entry
    if var_borrar.get():
        entNum.delete(0, tk.END)

# Layout (Frames)
frm = tk.Frame(root)
frm1 = tk.Frame(frm)
frm2 = tk.Frame(frm)
frm3 = tk.Frame(frm)

frm.pack(padx=10, pady=10)
frm1.pack(padx=10, pady=10)
frm2.pack(padx=10, pady=10)
frm3.pack(padx=10, pady=10)

# Widgets
lblEntry = tk.Label(frm1, text="Numero:")
entNum = tk.Entry(frm1, textvariable=var_num)
chkBorrar = tk.Checkbutton(frm1, text="Borrar?", variable=var_borrar)

lblEntry.grid(row=0, column=0, padx=5, pady=5)
entNum.grid(row=0, column=1, padx=5, pady=5)
chkBorrar.grid(row=0, column=2, padx=5, pady=5)

# Botones con Lambda para pasar el factor de multiplicación
btnXDos = tk.Button(frm2, text="x2", width=6, command=lambda:print_mult(2))
btnXTres = tk.Button(frm2, text="x3", width=6, command=lambda:print_mult(3))
btnXCinco = tk.Button(frm2, text="x5", width=6, command=lambda:print_mult(5))

# Radios con command=set_color para cambiar el color al instante
rdoNegro = tk.Radiobutton(frm2, text="Negro", variable=var_color, value=0, command=set_color)
rdoRojo = tk.Radiobutton(frm2, text="Rojo", variable=var_color, value=1, command=set_color)
rdoAzul = tk.Radiobutton(frm2, text="Azul", variable=var_color, value=2, command=set_color)

btnXDos.grid(row=0, column=0, padx=5, pady=5)
btnXTres.grid(row=0, column=1, padx=5, pady=5)
btnXCinco.grid(row=0, column=2, padx=5, pady=5)
rdoNegro.grid(row=1, column=0, padx=5, pady=5)
rdoRojo.grid(row=1, column=1, padx=5, pady=5)
rdoAzul.grid(row=1, column=2, padx=5, pady=5)

lblResultado = tk.Label(frm3, text="Resultado: {:5}".format(""), font="Arial 10")
lblResultado.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()


# ==============================================================================
# EJEMPLO 11: SIGN UP WINDOW (APP FINAL)
# ==============================================================================
print(">> Ejemplo 11: Sign Up App. Login, validación y persistencia en archivo.")

# Constantes simulando una base de datos o config
LOGIN = 'elviolado'
EMAIL = 'elado@mail.com'
PASSWORD = 'elvioforever'
FILE = "login.tmp" # Archivo temporal para recordar la sesión

root = tk.Tk()
root.title("tkinter App - Sign Up")
root.resizable(0, 0)

# Variables de Control
var_login = tk.StringVar()
var_email = tk.StringVar()
var_password = tk.StringVar()
var_confirm = tk.StringVar()
var_remember = tk.BooleanVar()

# Lógica de "Recordarme" al iniciar
# Intentamos abrir el archivo. Si no existe, el try...except lo maneja (pass)
try:
    with open(FILE) as file:
        check = file.read()
        if check.strip() == 'y':
            var_remember.set(True)
except:
    pass

# Si recordarme era True, pre-llenamos los campos
if var_remember.get():
    var_login.set(LOGIN)
    var_email.set(EMAIL)
            
# Función principal de registro
def sign_up():
    # Validamos que no haya campos vacíos
    if len(var_login.get()) > 0 and len(var_email.get()) > 0 and len(var_password.get()) > 0 and len(var_confirm.get()) > 0:
        # Validamos que los passwords coincidan
        if var_password.get() == var_confirm.get():
            # Validamos contra nuestras "constantes" (simulando backend)
            if var_login.get() == LOGIN and var_email.get() == EMAIL and var_password.get() == PASSWORD:
                messagebox.showinfo("Sign Up", "Credenciales Confirmadas. Bienvenido")
                
                # Gestión del archivo de persistencia (Guardar preferencia de 'Remember Me')
                with open(FILE, mode='w') as f:
                    if var_remember.get():
                        f.write('y')
                    else:
                        f.write('n')
                return # Salimos si todo fue bien
                
            else:
                messagebox.showerror("Sign Up Error", "Las credenciales ingresadas no son validas")
        else:
            messagebox.showerror("Confirmación de password", "Las contraseñas ingresadas no coinciden")
    else:
        messagebox.showerror("Error", "Debe de completar todos los campos")
    
    # Limpieza de campos si hubo error (excepto si fue exitoso, que ya retornó antes)
    entLogin.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPassword.delete(0, tk.END)
    entConfirm.delete(0, tk.END)
    

# Layout
frm = tk.Frame(root)
frmUp = tk.Frame(frm)
frmDown = tk.Frame(frm)

frm.pack(padx=10, pady=10)
frmUp.pack(padx=10, pady=10, anchor=tk.W)
frmDown.pack(padx=10, pady=10, anchor=tk.N)

# Widgets
# --------------------------- frmUp ----------------------------
lblSignUp = tk.Label(frmUp, text="Sign Up" , font="Arial 12 bold")
lblSignUp.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# ------------------------- frmDown ----------------------------
lblLogin = tk.Label(frmDown, text="        Login:")
lblEmail = tk.Label(frmDown, text="        Email:")
lblPassword = tk.Label(frmDown, text="        Password:")
lblConfirm = tk.Label(frmDown, text="         Confirm:")

# Entry con show='*' para ocultar caracteres (passwords)
entLogin = tk.Entry(frmDown, width=30, textvariable=var_login)
entEmail = tk.Entry(frmDown, width=30, textvariable=var_email)
entPassword = tk.Entry(frmDown, width=30, textvariable=var_password, show='*')
entConfirm = tk.Entry(frmDown, width=30, textvariable=var_confirm, show='*')

chkRemember = tk.Checkbutton(frmDown, text="Remember Me", variable=var_remember)
btnSignUp = tk.Button(frmDown, text="SignUp", width=12, command=sign_up)

# Grid Layout
lblLogin.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
lblEmail.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
lblPassword.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
lblConfirm.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

entLogin.grid(row=0, column=1, padx=5, pady=5)
entEmail.grid(row=1, column=1, padx=5, pady=5)
entPassword.grid(row=2, column=1, padx=5, pady=5)
entConfirm.grid(row=3, column=1, padx=5, pady=5)

chkRemember.grid(row=4, column=1, pady=5, sticky=tk.W)
btnSignUp.grid(row=3, column=2, padx=20, pady=5)

print("App ejecutándose. Recuerda probar las credenciales (están en el código al inicio de este bloque).")
root.mainloop()