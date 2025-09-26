# -*- coding: utf-8 -*-ç

#INDICAMOS QUE LOS PARAMETROS SON DE TIPO ENTERO
#LA FUNCION RETORNA UN ENTERO ->
def dias_mes(mes: int, anio: int) -> int:
    # Retorna el numero de dias de una mes
    if mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            return 29
        else:
            return 28
    elif mes in (4, 6, 9, 11):
        return 30
    else:
        return 31


def nombre_mes(mes: int) -> str:
    # Retorna un str con el nombre de la funcion
    return ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 
            'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 
            'SETIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 
            'DICIEMBRE'][mes]


def dia_primero(mes: int, anio: int) -> int:
    # Retorna el dia del 1ro del mes segun DOM=0, LUN=2, ... SAB=6
    if mes == 1 or mes == 2:
        mes += 12
        anio -= 1

    # Se obtiene el dia de la semana del 1ro del mes
    h = (1 + (13 * (mes + 1) // 5) + anio + (anio // 4) - (anio // 100) + (anio // 400)) % 7
    return (h + 6) % 7


def calendario_mes(mes: int, anio: int) -> list[list[str]]:
    dia_ini = dia_primero(mes, anio)
    dias_tot = dias_mes(mes, anio)
    lista_dias = [''] * 42
    lista_dias[dia_ini:dia_ini+dias_tot] = range(1, dias_tot + 1)
    lista_dias = list(map(lambda x: str(x), lista_dias))
    
    mes = []
    for idx in range(0, 42, 7):
        mes.append(lista_dias[idx:idx+7])
        
    return mes

