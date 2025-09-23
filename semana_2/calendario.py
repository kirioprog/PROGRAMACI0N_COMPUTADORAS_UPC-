m, y = input("Ingrese una fecha [mm/YYYY]: ").split("/")
m = int(m)
y = int(y)
q = 1

#obtenemos el numero de dias del mes

if m == 2:
    #PARA FEBRERO EN BISIESTO
    if y % 4 == 0 and ( y % 100 != 0 or y % 400 == 0):
        dias_mes = 29
    #SI FEBRERO NO ES BISIESTO
    else:
        dias_mes = 28
#MESES CON 30 DIAS 
elif m == 4 or m == 6 or m == 9 or m == 11:
    dias_mes = 30
else:
    dias_mes = 31

#IMPRIMIR EL MES
print("\n\t", end = '')

match m:
    #se imrpime el mes y el año
    case 1:print("ENERO",y)
    case 2:print("FEBRERO",y)
    case 3:print("MARZO",y)
    case 4:print("ABRIL",y)
    case 5:print("MAYO",y)
    case 6:print("JUNIO",y)
    case 7:print("JULIO",y)
    case 8:print("AGOSTO",y)
    case 9:print("SEPTIEMBRE",y)
    case 10:print("OCTUBRE",y)
    case 11:print("NOVIEMBRE",y)
    case 12:print("DICIEMBRE",y)

#Imprimimos los dias de la semana
print(f"\n\t{'D':>2}  {'L':>2}  {'M':>2}  {'X':>2}  {'J':>2}  {'V':>2}  {'S':>2}")

#ajustamos los valores del enero y febrero para utilizarlos en la formula
if m == 1 or m == 2 :
    m += 12
    y -=1
    
#CON LA FORMULA OBNTENEMOS EL DIA DE LA SEMANA DEL 1ER DEL MES X

h = (q + (13 * (m + 1) // 5) + y + (y // 4) - (y // 100) + (y // 400)) % 7
dia_ini = (h + 6) % 7

#VAMOS A IMPRIMIR TODOS LOS DIAS DEL CALENDARIO 
print("\t", end = '')  # Tab inicial para alinear
idx = 0                # Contador de posiciones (columnas)
dia = 1                # Número del día a imprimir

while dia <= dias_mes:  # Mientras no hayamos impreso todos los días del mes
    dia_str = ''       # String vacío por defecto
    
    if idx >= dia_ini:  # Si ya llegamos a la posición del día 1
        dia_str = str(dia)  # Convertimos el día a string
        dia += 1           # Avanzamos al siguiente día
    
    print(f"{dia_str:>2}  ", end='')  # Imprimimos (vacío o número)
    idx += 1  # Avanzamos a la siguiente columna
    
    if idx % 7 == 0:  # Cada 7 columnas (fin de semana)
        print("\n\t", end='')  # Nueva línea + tab
