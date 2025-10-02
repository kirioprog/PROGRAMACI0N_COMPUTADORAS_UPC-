# -*- coding: utf-8 -*-
from random import choice

def escoje_palabra():
    words = ['corriente',
            'voltaje', 
            'amperaje', 
            'resistencia', 
            'condensador', 
            'potencia', 
            'transistor', 
            'tiristor', 
            'varistor', 
            'diodo', 
            'triodo', 
            'amplificador', 
            'oscilador', 
            'histeresis', 
            'astable', 
            'bistable', 
            'compuerta', 
            'contador', 
            'registro', 
            'microchip', 
            'frecuencia', 
            'reactancia', 
            'ohmios', 
            'resonancia', 
            'modulacion', 
            'codificacion', 
            'capacitor', 
            'inductancia', 
            'filtrado', 
            'arreglo', 
            'resolucion', 
            'espectro', 
            'memoria', 
            'almacenamiento', 
            'impresora', 
            'pantalla', 
            'operacional', 
            'controlador', 
            'piezoelectrico', 
            'senoidal', 
            'digital', 
            'analogico']
    return choice(words)


def index_letra(texto: str, letra: str) -> list[int]:
    out = []
    for idx, char in enumerate(texto):
        if letra.upper() == char.upper():
            out.append(idx)
    else:
        return out


def show_hangman(idx):
    hangman = ["""
                   ----------
                   |         |
                   |         O
                   |
                   |
                   |
                   |
                   |
                   |
               ----------
               """, 
               """
                   ----------
                   |         |
                   |         O
                   |         |
                   |
                   |
                   |
                   |
                   |
               ----------
                """,
                """
                   ----------
                   |         |
                   |         O
                   |        /|
                   |
                   |
                   |
                   |
                   |
               ----------
                 """,
                 """
                   ----------
                   |         |
                   |         O
                   |        /|\\
                   |
                   |
                   |
                   |
                   |
               ----------
                  """,
                  """
                   ----------
                   |         |
                   |         O
                   |        /|\\
                   |         |
                   |
                   |
                   |
                   |
               ----------
                   """,
                   """
                   ----------
                   |         |
                   |         O
                   |        /|\\
                   |         |
                   |        /
                   |
                   |
                   |
               ----------
                    """,
                    """
                  ----------
                  |         |
                  |         O
                  |        /|\\
                  |         |
                  |        / \\
                  |
                  |
                  |
              ----------
                     """,]
                
    print(hangman[idx])