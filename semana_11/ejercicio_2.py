# -*- coding: utf-8 -*-
#Solo complete el código donde se debe (no cambie la estructura del programa)
import numpy as np

a = 1.55
N = 12

#arreglo de tiempos
#con linspace podemos generar un array con float. en este caso el reto te presenta 12 tiempos (revisa) 
t = np.linspace(0,10,12 )

#arreglo de velocidades
v = np.array(a * t)

#arreglo de distancia
d = 0.5 * a * t**2
#velocidad entre 6 y 10 m/s

print("tiempo  distancia   velocidad")
for tiempo,distancia,velocidad in zip(t,d,v):
    print("{:.2f}\t{:6,.2f}\t{:10,.2f}".format(tiempo,distancia,velocidad))
    
print("\nTiempos donde el coche alcanzó velocidades en el intervalo [6,10] m/s")
#hacemos la conficion de filtrado 
vel_mayor = ((v >= 6) & (v <=10) )
#utilizamosn np.where para que nos de los indices, en donde se cumple la condificion vel_mayor
indices = np.where(vel_mayor)

#pon es indices[0] porque el np.where en esta caso te arroja una tupla de un elemento y para acceder a esta ponemos asi con el cero 
for temp in t[indices[0]]:
    print("{:.2f}".format(temp))