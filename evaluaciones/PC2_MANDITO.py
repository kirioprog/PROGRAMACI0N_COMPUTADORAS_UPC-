# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

valores = np.random.randint(1000,10000,100)

print(f"Arreglo formado: {valores}")

 
condicion3 = (valores % 3 == 0)
suma_val_3 = np.sum(valores[condicion3])

condicion_menor = (valores < 5000)
suma_menor_5000 = np.sum(valores[condicion_menor])


condicion_intervalo = (valores >= 4000) & (valores <= 8000)
suma_intervalo = np.sum(valores[condicion_intervalo])

ejex= np.array(['suma: multiplos de 3', ' suma:< 5000', 'suma : [4000;8000]'])

ejey = np.array([suma_val_3, suma_menor_5000, suma_intervalo])
plt.bar(ejex , ejey)
plt.show()