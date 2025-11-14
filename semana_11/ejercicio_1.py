# -*- coding: utf-8 -*-
#Solo complete el código donde se debe (no cambie la estructura del programa)
import numpy as np

A = 20000
r = 6.5

#n: arreglo de años       
#no hay necesidad de convertir el n a np.array porque al hacer arange este ya viene incluido  
n = np.arange(1,11 )
#B: arreglo de balances calculados
B = A*(1 + (r/100)) ** n



print("año      balance")
for anio, balance in zip(n, B):
    print("{:2}\t{:6,.2f}".format(anio,balance))