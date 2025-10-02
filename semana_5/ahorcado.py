# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime
from hangman_tools import escoje_palabra, index_letra, show_hangman

palabra_adivinar: str = escoje_palabra().upper()           # CASA
palabra_actual: list[str] = ['_'] * len(palabra_adivinar)  #['_', '_', '_', '_']

num_intentos: int = 0
max_intentos: int = 6
win_game: bool = False
end_playing: bool = False
start = datetime.now()

while not end_playing:
    # Lazo del juego
    os.system('cls')
    print(f"{'EL AHORCADO':^45}")
    print(f"{'===========':^45}")
    print()
    show_hangman(num_intentos)
        
    print()
    print("Palabra:", " ".join(palabra_actual))   # _ _ _ _
    print()
    
    # Se pide que ingrese una letra o una palabra
    letra_palabra = input("Letra o palabra: ")
    
    # Si se ingresa una letra y esta es parte de la palabra...
    if len(letra_palabra) == 1 and letra_palabra.upper() in palabra_adivinar:
        indices = index_letra(palabra_adivinar, letra_palabra)
        
        if indices:
            for indice in indices:
                palabra_actual[indice] = letra_palabra.upper()
                
        # ...revisar si se ha ganado el juego
        if "".join(palabra_actual) == palabra_adivinar:
            win_game = True
            end_playing = True
            
    # ...en caso se haya ingresado una palabra completa
    elif letra_palabra.upper() == palabra_adivinar:
        win_game = True
        end_playing = True
        
    else:
        print("No hay coincidencia")
        num_intentos += 1
        time.sleep(1)
        
        if num_intentos == max_intentos:
            end_playing = True
    
    
# He ganado el juego o he perdido?
if win_game:
    os.system('cls')
    print(f"{'EL AHORCADO':^45}")
    print(f"{'===========':^45}")
    print()
    show_hangman(num_intentos)
    
    end = datetime.now()
    
    print()
    print("Palabra:", f'{" ".join([char for char in palabra_adivinar])}')
    print()
    print(f"{'HAS GANADO EL JUEGO!!!'}: Tiempo {end-start}")
else:
    os.system('cls')
    print(f"{'EL AHORCADO':^45}")
    print(f"{'===========':^45}")
    print()
    show_hangman(num_intentos)
    print("NO ADIVINO LA PALABRA")
            
