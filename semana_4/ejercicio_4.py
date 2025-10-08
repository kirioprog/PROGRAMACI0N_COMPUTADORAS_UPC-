# -*- coding: utf-8 -*-
# tambien puede poner list[int,int]
def area(v1: list, v2: list, v3:list) -> float:
    area = 0.5 * (v2[0]*v3[1] - v3[0]*v2[1] - v1[0]*v3[1] + v3[0]*v1[1] + v1[0]*v2[1] - v2[0]*v1[1])
    return area

vertice = []
for idx in range(3):
    #Utilice map para convertir cada valor ingresado a un numero entero- separado por el separador ','
    vertice.append(list(map(int,input(f"Ingrese el vertice {idx} en el formato x,y : ").split(','))))
    #print(vertice)
    
v1, v2, v3 = vertice
print("El area del triangulo es: ",area(v1, v2, v3))
