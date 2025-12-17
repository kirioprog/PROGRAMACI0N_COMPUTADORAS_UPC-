# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import random
import csv
import os

# =============================================================================
# 1. CLASE CLIENTE (Requerimiento: Semana 10 - POO con Validaciones)
# =============================================================================
class Cliente:
    def __init__(self, nombre, montoPagado, referencia):
        # Al asignar a self.variable, se activan los setters automáticamente
        self.nombre = nombre
        self.montoPagado = montoPagado
        self.referencia = referencia

    # --- Propiedad: nombre ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, val):
        if isinstance(val, str):
            self._nombre = val
        else:
            raise TypeError("El nombre debe ser una cadena de texto (string).")

    # --- Propiedad: montoPagado ---
    @property
    def montoPagado(self):
        return self._montoPagado
    
    @montoPagado.setter
    def montoPagado(self, val):
        # Validamos que sea float y mayor a cero
        if isinstance(val, float) and val > 0:
            self._montoPagado = val
        else:
            raise ValueError("El monto pagado debe ser un flotante mayor a cero.")

    # --- Propiedad: referencia ---
    @property
    def referencia(self):
        return self._referencia
    
    @referencia.setter
    def referencia(self, val):
        # Debe ser string, tener 5 caracteres y ser numéricos
        if isinstance(val, str) and len(val) == 5 and val.isdigit():
            self._referencia = val
        else:
            raise ValueError("La referencia debe ser un string de 5 caracteres numéricos.")

# =============================================================================
# 2. LÓGICA Y VARIABLES GLOBALES
# =============================================================================
lista_clientes = []  # Aquí almacenaremos los objetos Cliente

# Precios unitarios según la tabla de la imagen
PRECIOS = {
    'Clasico': 11.9,
    'Doble Queso': 12.9,
    'Tocino': 14.9,
    'Royal': 15.9,
    'Parrillero': 16.9,
    'Light': 12.9
}

def generar_referencia_unica():
    """Genera 5 dígitos aleatorios y valida que no se repita en la lista."""
    while True:
        # Generamos número entre 0 y 99999, formateado con ceros a la izquierda
        ref_num = random.randint(0, 99999)
        ref_str = "{:05d}".format(ref_num)
        
        # Validar unicidad (Semana 2: in / bucles)
        existe = False
        for cliente in lista_clientes:
            if cliente.referencia == ref_str:
                existe = True
                break
        
        if not existe:
            return ref_str

def calcular_total():
    try:
        # 1. Obtener cantidades de los Entrys (IntVars)
        q_clasico = var_clasico.get()
        q_doble = var_doble.get()
        q_tocino = var_tocino.get()
        q_royal = var_royal.get()
        q_parrillero = var_parrillero.get()
        q_light = var_light.get()
        
        # Validar que no sean negativos (aunque IntVar suele manejarlo, es buena práctica)
        cantidades = [q_clasico, q_doble, q_tocino, q_royal, q_parrillero, q_light]
        for q in cantidades:
            if q < 0:
                raise ValueError("Las cantidades no pueden ser negativas.")
        
        # Validar que se haya ingresado al menos un item
        if sum(cantidades) == 0:
             messagebox.showwarning("Advertencia", "Debe seleccionar al menos un combo.")
             return

        # 2. Calcular Costo Bruto
        costo = (q_clasico * PRECIOS['Clasico'] +
                 q_doble * PRECIOS['Doble Queso'] +
                 q_tocino * PRECIOS['Tocino'] +
                 q_royal * PRECIOS['Royal'] +
                 q_parrillero * PRECIOS['Parrillero'] +
                 q_light * PRECIOS['Light'])
        
        # 3. Cálculos adicionales
        delivery = costo * 0.03
        impuesto = costo * 0.18
        total = costo + delivery + impuesto
        
        # Aplicar promoción si el Checkbutton está activo
        precio_final = total
        if var_promo.get():
            descuento = costo * 0.10
            precio_final = total - descuento

        # 4. Generar Referencia
        referencia = generar_referencia_unica()
        
        # 5. Obtener Nombre Cliente
        nombre = var_nombre_cliente.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Debe ingresar el nombre del cliente.")
            return

        # 6. Crear Objeto Cliente (esto activa las validaciones de la Clase)
        # Convertimos precio_final a float explícitamente y redondeamos visualmente después
        nuevo_cliente = Cliente(nombre, float(precio_final), referencia)
        
        # 7. Agregar a la lista
        lista_clientes.append(nuevo_cliente)
        
        # 8. Actualizar Interfaz Gráfica (Parte Derecha)
        var_ref_out.set(referencia)
        var_costo_out.set(f"{costo:.2f}")
        var_delivery_out.set(f"{delivery:.2f}")
        var_impuesto_out.set(f"{impuesto:.2f}")
        var_total_out.set(f"{total:.2f}")
        var_final_out.set(f"{precio_final:.2f}")
        
        # Habilitar botón reporte
        btn_reporte.config(state='normal')
        
    except ValueError as e:
        messagebox.showerror("Error de Valor", f"Ocurrió un error en los datos: {e}")
    except TypeError as e:
        messagebox.showerror("Error de Tipo", str(e))
    except Exception as e:
        # Captura genérica por si los Entry tienen texto no numérico
        messagebox.showerror("Error", "Verifique que las cantidades sean números enteros.")

def reset_app():
    # Resetear campos izquierda a 0
    var_clasico.set(0)
    var_doble.set(0)
    var_tocino.set(0)
    var_royal.set(0)
    var_parrillero.set(0)
    var_light.set(0)
    
    # Limpiar campos derecha
    var_ref_out.set("")
    var_costo_out.set("")
    var_delivery_out.set("")
    var_impuesto_out.set("")
    var_total_out.set("")
    var_final_out.set("")
    
    # Limpiar nombre y check
    var_nombre_cliente.set("")
    var_promo.set(False)
    
    # Deshabilitar botón reporte
    btn_reporte.config(state='disabled')

def generar_reporte():
    try:
        filename = "reporte.csv"
        # Semana 7: Manejo de Archivos CSV ('w' mode)
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file) # Por defecto usa coma como separador
            
            # Encabezado
            writer.writerow(["REFERENCIA", "NOMBRE", "MONTO PAGADO (soles)"])
            
            # Datos de los clientes almacenados
            for cli in lista_clientes:
                writer.writerow([cli.referencia, cli.nombre, f"{cli.montoPagado:.2f}"])
        
        messagebox.showinfo("Reporte", f"Archivo '{filename}' generado exitosamente con {len(lista_clientes)} registros.")
        
    except Exception as e:
        messagebox.showerror("Error Archivo", f"No se pudo crear el reporte: {e}")

# =============================================================================
# 3. INTERFAZ GRÁFICA (Tkinter - Semana 13 y 14)
# =============================================================================
root = tk.Tk()
root.title("Menu Cash Register")
root.geometry("550x350")
root.resizable(0, 0) # Ventana fija según imagen

# --- Variables de Control ---
# Entradas (Izquierda) - Cantidades
var_clasico = tk.IntVar(value=0)
var_doble = tk.IntVar(value=0)
var_tocino = tk.IntVar(value=0)
var_royal = tk.IntVar(value=0)
var_parrillero = tk.IntVar(value=0)
var_light = tk.IntVar(value=0)

# Salidas (Derecha) - Detalles (Usamos StringVar para actualizar Entrys disabled)
var_ref_out = tk.StringVar()
var_costo_out = tk.StringVar()
var_delivery_out = tk.StringVar()
var_impuesto_out = tk.StringVar()
var_total_out = tk.StringVar()
var_final_out = tk.StringVar()

# Cliente y Promo
var_nombre_cliente = tk.StringVar()
var_promo = tk.BooleanVar()

# --- Layout Principal ---
# Usaremos Frames para organizar (Izquierda, Derecha, Abajo)
frm_main = tk.Frame(root)
frm_main.pack(padx=10, pady=10)

frm_left = tk.Frame(frm_main)
frm_left.grid(row=0, column=0, padx=20, pady=10, sticky=tk.N)

frm_right = tk.Frame(frm_main)
frm_right.grid(row=0, column=1, padx=20, pady=10, sticky=tk.N)

frm_bottom = tk.Frame(root)
frm_bottom.pack(padx=10, pady=5)

# --- WIDGETS IZQUIERDA (Combos) ---
combos_data = [
    ("Combo Clasico", var_clasico),
    ("Combo Doble Queso", var_doble),
    ("Combo Tocino", var_tocino),
    ("Combo Royal", var_royal),
    ("Combo Parrillero", var_parrillero),
    ("Combo Light", var_light)
]

for idx, (text, var) in enumerate(combos_data):
    lbl = tk.Label(frm_left, text=text)
    lbl.grid(row=idx, column=0, sticky=tk.E, padx=5, pady=3)
    ent = tk.Entry(frm_left, textvariable=var, width=5)
    ent.grid(row=idx, column=1, padx=5, pady=3)

# --- WIDGETS DERECHA (Resultados) ---
# Entrys bloqueados (state='disabled')
resultados_data = [
    ("Referencia", var_ref_out),
    ("Costo", var_costo_out),
    ("Delivery", var_delivery_out),
    ("Impuesto", var_impuesto_out),
    ("Total", var_total_out),
    ("Precio Final", var_final_out)
]

for idx, (text, var) in enumerate(resultados_data):
    lbl = tk.Label(frm_right, text=text)
    lbl.grid(row=idx, column=0, sticky=tk.E, padx=5, pady=3)
    # state='disabled' impide escribir, pero textvariable permite actualizar valor desde código
    ent = tk.Entry(frm_right, textvariable=var, width=15, state='disabled') 
    ent.grid(row=idx, column=1, padx=5, pady=3)

# --- WIDGETS INFERIORES (Cliente y Botones) ---

# Nombre y Promo
lbl_nombre = tk.Label(frm_bottom, text="Nombre cliente")
lbl_nombre.grid(row=0, column=0, padx=5, pady=10)

ent_nombre = tk.Entry(frm_bottom, textvariable=var_nombre_cliente, width=20)
ent_nombre.grid(row=0, column=1, padx=5, pady=10)

chk_promo = tk.Checkbutton(frm_bottom, text="Aplicar promocion?", variable=var_promo)
chk_promo.grid(row=0, column=2, padx=15, pady=10)

# Botones
frm_btns = tk.Frame(root)
frm_btns.pack(pady=10)

btn_total = tk.Button(frm_btns, text="Total", width=10, command=calcular_total)
btn_total.grid(row=0, column=0, padx=10)

btn_reset = tk.Button(frm_btns, text="Reset", width=10, command=reset_app)
btn_reset.grid(row=0, column=1, padx=10)

# Reporte inicia deshabilitado
btn_reporte = tk.Button(frm_btns, text="Reporte", width=10, command=generar_reporte, state='disabled')
btn_reporte.grid(row=0, column=2, padx=10)


# Iniciar Loop
if __name__ == "__main__":
    root.mainloop()  