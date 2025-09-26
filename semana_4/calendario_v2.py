# -*- coding: utf-8 -*-
#IMPORTAMOS SOLO LAS FUNCIONES QUE NECESITAREMOS 
from func_calcendar import calendario_mes, nombre_mes

opc = input("Calendario Anual [a] o Calendario Mensual [m]: ")

if opc == 'm':
    m, Y = input("Ingrese una fecha [mm/YYYY]: ").split("/")
    m = int(m)
    Y = int(Y)
    
    # Impresion el encabezado del calendario
    print(f"\n\t{nombre_mes(m-1)}", end='')    
    print(f"\n\t{'D':>2}  {'L':>2}  {'M':>2}  {'X':>2}  {'J':>2}  {'V':>2}  {'S':>2}")
    
    # Imprimir el calendario
    for week in calendario_mes(m, Y):
        print("\t{:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}".format(*week))
    else:
        print()
        
        
elif opc == 'a':
    Y = int(input("Ingrese el año: "))
    anio = [calendario_mes(mes, Y) for mes in range(1, 13)]
    
    # Impresion del calendario anual
    print(f"\n  {Y:^102}")
    print()
    
    # Se imprime en tres columnas los nombres de los meses
    for idx in range(0, 12, 3):
        for idx_mes in range(3):
            print(f"\t{nombre_mes(idx + idx_mes):10}", end='')
            print(" " * 20, end='')
        else:
            print()
            
        # Imprime el encabezado de las columnas por mes
        for _ in range(3):
            print(f"\t{'D':>2}  {'L':>2}  {'M':>2}  {'X':>2}  {'J':>2}  {'V':>2}  {'S':>2}     ", end='')
        else:
            print()
    
    
        mes1, mes2, mes3 = anio[idx:idx+3]
        for sem_mes1, sem_mes2, sem_mes3 in zip(mes1, mes2, mes3):
            print("\t{:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}    ".format(*sem_mes1), end='')
            print("\t{:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}    ".format(*sem_mes2), end='')
            print("\t{:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}    ".format(*sem_mes3))
        else:
            print()

else:
    print("Opcion invalida")






