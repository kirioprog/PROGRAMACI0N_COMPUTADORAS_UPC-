# Escriba un programa que tenga dos lazos for anidados (un for dentro de otro for) y que muestre los valores enteros del 1 a 100, alineados tal como se muestra:

# 1    2    3    4    5    6    7    8    9   10
#11   12   13   14   15   16   17   18   19   20
#21   22   23   24   25   26   27   28   29   30
#91   92   93   94   95   96   97   98   99  100
n = 1
for numeracion in range(0,10):
    print("\t")
    for fila in range(n,n+10):
        print(f'{fila:>4}\t', end = '')
    n += 10 
    
#%%

# Programa que determina la etapa de vida de una persona según su edad
# El programa pide el nombre de una persona y luego su edad
# Valida que la edad debe ser mayor a 0 y además un número entero
# De lo contrario se deberá volver a pedir
# Luego del ingreso, el programa muestra la etapa de la vida de la persona

# Etapas de vida según los intervalos de edad:
# edad en el intervalo [1,3] años  es bebe
# edad en el intervalo [4,11] años es niño  
# edad en el intervalo [12,17] años es adolescente
# edad en el intervalo [18,30] años es adulto joven
# edad en el intervalo [31,60] años es adulto
# edad en el intervalo 61 a mas años es adulto mayor
valor = False
nombre = input("Ingrese el nombre de la persona: ")
while not valor :
    try:
        #si edad es correcto, osea numero entero pasa al if
        #si edad no es numero entero pasa  a except 
        edad = int(input("Ingrese su edad: "))
    except:
        print("La edad debe ser un numero entero")
        #continue va omitir todo el codigo de abajo sin importar jerarquia pero pertence a          while 
        continue
    
    if edad < 0 :
        print("Ingrese un numero mayor a 0")
    else: 
        valor = True 
        if 1 <= edad <= 3 :
            print("ES bebe ")
        elif 4 <= edad <= 11 :
            print("Es niño ")
        elif 12 <= edad <= 17 :
            print("Es adoslecente")
        elif 18 <= edad <= 30 :
            print("Es adulto joven")
        elif 31 <= edad <= 60 :
            print("Es adulto")
        else:
            print("Es adulto mayor")


        
    
            
