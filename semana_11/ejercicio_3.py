# -*- coding: utf-8 -*-
#Solo complete el código donde se debe (no cambie la estructura del programa)

import numpy as np

velArena = 3.5
velCamino = 5
w = 4.5
u = 14

#teta: arreglo de angulos (en grados)
teta = np.arange(0,61,10)

#ang: arreglo de angulos (en radianes)
ang = teta * (np.pi/180)

#tiempos:  arreglo de tiempos calculados

tiempos = ((1/np.cos(ang))* w)/velArena + (u - w*np.tan(ang))/velCamino


print("angulo(grados)   tiempo")
for angulo,t in zip(teta,tiempos):
    print("{:8.2f}\t{:6.3f}".format(angulo,t))