#calculador de IMC 
#CREAR UN RANDOM DE PESOS DE 45 A 110
import random
for cantidad in range(50):
    #crea valores random enteros en el rango de 45 a 110
    peso = random.randrange(45, 110)
    #crea valores random de tipo float en el rango de 1.5 a 1.8 
    altura = random.uniform(1.5, 1.8)
    
    #calcular el IMC
    imc = peso/ (altura ** 2)
    if imc < 18.5 :
        estado = "Bajo peso"
    elif imc < 25 :
        estado = "Peso Normal"
    elif imc < 30 :
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
        
        
    
    print(f"{cantidad + 1:<3}|  Peso: {peso:<3}Kg  Altura: {altura:<3.2f}m  IMC: {imc:.2f}  Estado: {estado}")
    
