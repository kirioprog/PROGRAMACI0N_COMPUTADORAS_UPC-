import csv

def leerArchivo(nombreArchivo):
    lista = []
    with open(nombreArchivo, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        if reader.fieldnames[0].startswith('\ufeff'):
            reader.fieldnames[0] = reader.fieldnames[0][1:]
        for fila in reader:
            d = {
                "codigo": fila["Código"],
                "nombre": fila["Nombre"],
                "apellido": fila["Apellido"],
                "escuela": fila["Escuela"],
                "EP": float(fila["EP"]),
                "EF": float(fila["EF"])
            }
            lista.append(d)
    return lista

def determinaEscuela(listaDi):
    conteo = {}
    for alumno in listaDi:
        escuela = alumno["escuela"]
        conteo[escuela] = conteo.get(escuela, 0) + 1
    max_cant = max(conteo.values())
    escuela_max = [idx for idx, cant in conteo.items() if cant == max_cant]
    return escuela_max

def determinaMayorMenor(listaD):
    notas = [0.4*alumno["EP"] + 0.6*alumno["EF"] for alumno in listaD]
    return (min(notas), max(notas))

def mostrarAprobados(listaD, minima):
    aprobados = []
    for alumno in listaD:
        nf = 0.4*alumno["EP"] + 0.6*alumno["EF"]
        if nf >= minima:
            aprobados.append((alumno["codigo"], alumno["nombre"], alumno["apellido"], nf))
    aprobados.sort(key=lambda x: x[1])
    print(f"{'Codigo':<8} {'Nombre':<10} {'Apellido':<12} {'NF':>5}")
    for cod, nom, ape, nf in aprobados:
        print(f"{cod:<8} {nom:<10} {ape:<12} {nf:5.2f}")


archivo = "alumnos.csv"
lista = leerArchivo(archivo)

escuela_max = determinaEscuela(lista)
print("Reporte 1: Escuelas profesionales con mayor cantidad de alumnos:")
for idx in escuela_max:
    print(f" - {idx}")
print()


nf_min, nf_max = determinaMayorMenor(lista)
print(f"Reporte 2: Nota final minima: {nf_min:.2f}")
print(f"           Nota final maxima: {nf_max:.2f}")
print()


print("Reporte 3: Alumnos aprobados:")
mostrarAprobados(lista, 12.5)