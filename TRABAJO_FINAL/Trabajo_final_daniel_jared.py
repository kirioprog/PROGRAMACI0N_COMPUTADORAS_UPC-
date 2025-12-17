import tkinter as tk
from tkinter import messagebox
import random
import csv

class Cliente:
    def __init__(self, nombre, monto, referencia):
        self.nombre = nombre
        self.montoPagado = monto
        self.referencia = referencia

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self._nombre = valor
        else:
            raise TypeError("El nombre debe ser texto")

    @property
    def montoPagado(self):
        return self._montoPagado
    
    @montoPagado.setter
    def montoPagado(self, valor):
        if isinstance(valor, float) and valor > 0:
            self._montoPagado = valor
        else:
            raise ValueError("Monto debe ser mayor a 0")

    @property
    def referencia(self):
        return self._referencia
    
    @referencia.setter
    def referencia(self, valor):
        if isinstance(valor, str) and len(valor) == 5 and valor.isdigit():
            self._referencia = valor
        else:
            raise ValueError("Referencia incorrecta")

lista_clientes = []
lista_precios = [11.9, 12.9, 14.9, 15.9, 16.9, 12.9]

def calcular():
    try:
        lista_cantidades = [clasico.get(), doble.get(), tocino.get(), 
                            royal.get(), parrillero.get(), light.get()]
        
        if sum(lista_cantidades) == 0:
            messagebox.showwarning("Alerta", "Seleccione al menos un combo")
            return

        costo = 0
        for i in range(6):
            if lista_cantidades[i] < 0:
                raise ValueError("No negativos")
            costo += lista_cantidades[i] * lista_precios[i]

        delivery = costo * 0.03
        impuesto = costo * 0.18
        total = costo + delivery + impuesto
        final = total

        if promocion.get():
            final = total - (costo * 0.10)

        while True:
            ref = "{:05d}".format(random.randint(0, 99999))
            existe = False
            for cliente in lista_clientes:
                if cliente.referencia == ref:
                    existe = True
            if not existe:
                break
        
        dato_nombre = nombre_cliente.get().strip()
        if dato_nombre == "":
            raise TypeError("Falta nombre")

        nuevo_cliente = Cliente(dato_nombre, float(final), ref)
        lista_clientes.append(nuevo_cliente)

        texto_referencia.set(ref)
        texto_costo.set(f"{costo:.2f}")
        texto_delivery.set(f"{delivery:.2f}")
        texto_impuesto.set(f"{impuesto:.2f}")
        texto_total.set(f"{total:.2f}")
        texto_final.set(f"{final:.2f}")

        boton_reporte.config(state='normal')

    except Exception as error:
        messagebox.showerror("Error", str(error))

def limpiar():
    clasico.set(0)
    doble.set(0)
    tocino.set(0)
    royal.set(0)
    parrillero.set(0)
    light.set(0)
    
    texto_referencia.set("")
    texto_costo.set("")
    texto_delivery.set("")
    texto_impuesto.set("")
    texto_total.set("")
    texto_final.set("")
    
    nombre_cliente.set("")
    promocion.set(False)
    boton_reporte.config(state='disabled')

def reporte():
    try:
        with open("reporte.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["REFERENCIA", "NOMBRE", "MONTO PAGADO (soles)"])
            for cliente in lista_clientes:
                escritor.writerow([cliente.referencia, cliente.nombre, f"{cliente.montoPagado:.2f}"])
        messagebox.showinfo("Info", "Reporte creado")
    except:
        messagebox.showerror("Error", "Error en archivo")

root = tk.Tk()
root.title("Menu Cash Register")
root.geometry("550x350")

clasico = tk.IntVar()
doble = tk.IntVar()
tocino = tk.IntVar()
royal = tk.IntVar()
parrillero = tk.IntVar()
light = tk.IntVar()

texto_referencia = tk.StringVar()
texto_costo = tk.StringVar()
texto_delivery = tk.StringVar()
texto_impuesto = tk.StringVar()
texto_total = tk.StringVar()
texto_final = tk.StringVar()

nombre_cliente = tk.StringVar()
promocion = tk.BooleanVar()

marco_principal = tk.Frame(root)
marco_principal.pack(pady=10)

marco_izq = tk.Frame(marco_principal)
marco_izq.pack(side=tk.LEFT, padx=20)

marco_der = tk.Frame(marco_principal)
marco_der.pack(side=tk.LEFT, padx=20)

marco_abajo = tk.Frame(root)
marco_abajo.pack(pady=5)

lista_etiquetas = ["Combo Clasico", "Combo Doble Queso", "Combo Tocino", 
                   "Combo Royal", "Combo Parrillero", "Combo Light"]
lista_variables = [clasico, doble, tocino, royal, parrillero, light]

for i in range(6):
    tk.Label(marco_izq, text=lista_etiquetas[i]).grid(row=i, column=0, sticky='e')
    tk.Entry(marco_izq, textvariable=lista_variables[i], width=5).grid(row=i, column=1)

lista_salidas = ["Referencia", "Costo", "Delivery", "Impuesto", "Total", "Precio Final"]
lista_textos = [texto_referencia, texto_costo, texto_delivery, texto_impuesto, texto_total, texto_final]

for i in range(6):
    tk.Label(marco_der, text=lista_salidas[i]).grid(row=i, column=0, sticky='e')
    tk.Entry(marco_der, textvariable=lista_textos[i], state='disabled', width=15).grid(row=i, column=1)

tk.Label(marco_abajo, text="Nombre cliente").grid(row=0, column=0)
tk.Entry(marco_abajo, textvariable=nombre_cliente, width=20).grid(row=0, column=1, padx=5)
tk.Checkbutton(marco_abajo, text="Aplicar promocion?", variable=promocion).grid(row=0, column=2)

marco_botones = tk.Frame(root)
marco_botones.pack(pady=10)
tk.Button(marco_botones, text="Total", command=calcular, width=10).grid(row=0, column=0, padx=5)
tk.Button(marco_botones, text="Reset", command=limpiar, width=10).grid(row=0, column=1, padx=5)
boton_reporte = tk.Button(marco_botones, text="Reporte", command=reporte, width=10, state='disabled')
boton_reporte.grid(row=0, column=2, padx=5)

root.mainloop()