# -*- coding: utf-8 -*-
import random


lista_lista = [[(f"{random.uniform(0.5,1.5):.3f}") for idx in range(5)] for cantidad in range(10)]
#lista = [(f"{random.uniform(0.5,1.5):.3f}") for idx in range(5)]



for idx in range(10):
    #desempaquetamos cada lista de lista_lista
    print(f"lista {idx + 1:>2}:", *lista_lista[idx], sep=', ' )
