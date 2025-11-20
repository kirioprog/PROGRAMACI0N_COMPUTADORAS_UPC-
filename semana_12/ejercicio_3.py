# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

r = 4
l = 1.3
v = 12
t = np.linspace(0, 2, 20)

# CORRECCIÓN 1: Inicializar con ceros del mismo tamaño que t
i = np.zeros_like(t) 

# Calculamos el argumento del exponente para todo t
# Nota: Matemáticamente esto es -t/tau (donde tau de tiempo es L/R)
arg_exp = (-1 * r * t) / l 

# CORRECCIÓN 2: Paréntesis obligatorios
t_rank1 = (t >= 0) & (t <= 0.5)


#Accedemos a las ubicaciones t_rank1 en donde sto es verdadero, por eso pongo i[t_ran1] porque en esos espacios se llenara con el valro que pongo al costado 
# Si no pones [t_rank1] dentro de exp(), intentará meter 20 datos en 5 huecos.
i[t_rank1] = (v/r) * (1 - np.exp(arg_exp[t_rank1]))

# Segundo tramo
t_rank2 = (t > 0.5) # Usamos > para no sobreescribir el 0.5

# Lo mismo aquí: aplicamos el filtro [t_rank2] al argumento de la exponencial
i[t_rank2] = np.exp(arg_exp[t_rank2]) * (v/r) * (np.exp(0.5*r/l) - 1)

print(i)

# Graficamos para que veas que funciona
plt.plot(t, i, 'o-') # 'o-' para ver los puntos
plt.grid(True)
plt.show()