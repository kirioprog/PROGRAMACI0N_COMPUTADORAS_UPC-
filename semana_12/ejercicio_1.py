# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#Creamos un np del rango de 1- 10,  POR DEFECTO TIENE 50 DIVISIONES
#como consecuencia luego vas a VER 20 PUNTITOS EN LA GRAFICA 
rl = np.linspace(1, 10,20)
vs = 12
rs = 2.5

p = ((vs ** 2) * rl) / ((rl + rs) ** 2)


#verificamos
print(p)
print()
print(rl)
for idx, potencia in enumerate (p , start = 1):
    print(f"{idx} -> {potencia}")

#mostramos el valor de la potenica maxima, para ello vamos a filtrar la potenica maxima
p_max = np.max(p)
print(f"La potencia maxima disipada es {p_max}")
#mostrar el valor en donde se produce esa maximqa transferencia de potencia
indice = np.argmax(p)
print(f"El rl en donde se produce la maxima tranferenica de potencia es en {rl[indice]}")

#Vamos a graficar
plt.plot(rl,p, '-bo')
plt.title("Circuito RL")
plt.xlabel("Resistencia del inductor")
plt.ylabel("Maxima potencia")
plt.grid()
plt.show()