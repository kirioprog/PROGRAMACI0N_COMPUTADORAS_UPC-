import csv

archivo = "alumnos.csv"

# Variables de cálculo
conteo_escuelas = {}
nota_min = 999
nota_max = -1
aprobados = []

with open(archivo, encoding='utf-8') as file:
    reader = csv.DictReader(file)



    # Recorrido directo al estilo del primer código
    for fila in reader:

        # Cálculo de NF por alumno
        ep = float(fila["EP"])
        ef = float(fila["EF"])
        nf = 0.4*ep + 0.6*ef

        # Contamos por escuela
        escuela = fila["Escuela"]
        conteo_escuelas[escuela] = conteo_escuelas.get(escuela, 0) + 1

        # Actualizamos min/max
        if nf < nota_min: nota_min = nf
        if nf > nota_max: nota_max = nf

        # Guardamos aprobados
        if nf >= 12.5:
            aprobados.append((fila["Código"], fila["Nombre"], fila["Apellido"], nf))

# --- Reportes ---

# Reporte 1
print("Reporte 1: Escuelas con más alumnos:")
max_cant = max(conteo_escuelas.values())
for esc, cant in conteo_escuelas.items():
    if cant == max_cant:
        print(f" - {esc}")
print()

# Reporte 2
print(f"Reporte 2: Nota final mínima: {nota_min:.2f}")
print(f"           Nota final máxima: {nota_max:.2f}")
print()

# Reporte 3
print("Reporte 3: Alumnos aprobados:")
aprobados.sort(key=lambda x: x[1])  # orden por nombre

print(f"{'Codigo':<8} {'Nombre':<10} {'Apellido':<12} {'NF':>5}")
for cod, nom, ape, nf in aprobados:
    print(f"{cod:<8} {nom:<10} {ape:<12} {nf:5.2f}")
