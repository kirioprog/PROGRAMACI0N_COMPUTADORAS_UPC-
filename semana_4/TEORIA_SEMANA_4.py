#SEMANA 4

#%%

#FUNCIONES

#CREAR UNA FUNCION Y EXPLICAR LO QUE HACE LA FUNCION 

def suma_num(num1, num2):
    #Entre las 3 comilla escribimos como funciona la funcion de manera textual 
    ''' suma_num(num1, num2): Retorma la suma de los numeros ingresados
    
    PARAMETROS:
        num1, num2: int
        
    USO:
        suma_num(3, 5) -> 8
    '''
    #Una vez escrito como funciona la funcion que creaste puedes ver esto ingresadno a la terminal suma_num?
    
    #RETORNA LA SUMA DE NUM1 Y NUM2
    return num1 + num2

print(suma_num(3, 5))
#%%
#VARIABLES Y FUNCIONES LOCALES 
nombre = "Kirio"

def cambia_nombre():
    #esta variable nombre solo tiene alcance local osea solo exist e dentro de la funcion 
    #DEFINIAMOS EL ALCANCE GLOBAL PARA LA VARIABLE NOMBRE
    global nombre 
    nombre = "Saho"
    
    
    
#poner cambia_nombre() en esta ubicacion es porque estamos llamando a la funcion PARAA QUE SE EJECUTE
cambia_nombre()
print(nombre)

#%%
#REGLA LEGB:
    #LOCAL ( dentro de una funcion)
    #ENCLOSING (funcion que contiene a otra funcion)
    #GLOBAL(nivel archivo)
#LOCAL>ENCLOSING>GLOBAL
    

# Declaro una variable en el ámbito GLOBAL del programa
var = "var global"

# Defino una función llamada fun_externa (como declarar void fun_externa() en C)
def fun_externa():
    # Dentro de fun_externa, creo una variable LOCAL llamada var
    # Esta var "tapa" a la var global (solo dentro de esta función)
    var = "var externa"
    
    # Dentro de fun_externa, defino OTRA función llamada fun_interna
    # Es como tener una función dentro de otra función
    def fun_interna():
        # Dentro de fun_interna, creo OTRA variable LOCAL llamada var
        # Esta var "tapa" tanto a la var de fun_externa como a la global
        var = "var interna"
        # Imprimo la var más cercana que encuentro (la LOCAL de fun_interna)
        print(var)  # Imprime: "var interna"
        
    # Aquí termina la DEFINICIÓN de fun_interna, pero aún no se ejecuta    
    
    # EJECUTO fun_interna (como llamar una función en main de C)
    # Esto hace que se ejecute todo el código dentro de fun_interna
    fun_interna()
    
    # Imprimo la var más cercana en fun_externa (su propia var LOCAL)
    # NO ve la var de fun_interna porque ya salí de esa función
    print(var)  # Imprime: "var externa"

# Aquí termina la DEFINICIÓN de fun_externa, pero aún no se ejecuta

# EJECUTO fun_externa (como llamar una función en main de C)
# Esto ejecuta todo el código dentro de fun_externa
fun_externa()
 #%%
#KEYWORDS

def num_suma(num1, num2):
    return num1 + num2


print(num_suma(3,4))

#ojo QUE PASA CON LA FUNCION SUMA ? 
#LA QUE YA VIENE DEFINIDA CON PYTHON 

#    sum(iterable, start=0) el star es  en donde empieza a sumar


print(sum([1,2,3,4,5])) #Suma todos los valores de la lista

#en la siguiente suma empieza a sumar desde 10
print(sum([1, 2, 3, 4, 5], 10))

#APLIQUEMOS KEYWORDS
#espécificamos con el nombre del parametro nada mas 
print(sum([1, 2, 3, 4, 5], start=10))

#%%
#RETOMAR MAS DE 1 VALOR 
def mult_div(num1, num2):
    #vamos a retormar el producto y la division, cada retorna se separa por una coma
    
    #TE LO RETORNA EN FORMA DE TUPLA 
    return num1 * num2, num1 / num2

print(mult_div(8,4))

#imprimamos cada valor por separado 
resultado = mult_div(8, 4)
print(resultado[0])
print(resultado[1])

#TAMBIEN LO PUEDES HACER DESEMPAQUETANDO LAS TUPLAS
print()
m, d = mult_div(8, 4)
print(m)
print(d)

#%%
#PARAMETROS INFINITOS PARA UNA FUNCION

#PRIMERO REVISEMOS COMO FUNCIONA EL OPERADOR SPLAT
nums = [10, 20, 30]

print(nums)
#el splat desempaqueta una una lista o tupla 
print(*nums)

print()

def suma_todo(*args):
    return sum(args)

print(suma_todo(1))
print(suma_todo(1,2,3,4,5))

#%%
 #FUNCIONES RECURSIVAS 
 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#%%FUNCIONES ANONIMAS

def por_tres(n):
    return 3 * n

print(por_tres(5))

#AHORA UTILICEMOS UNA FUNCION ANONIMA LAMBDA
#SON FUNCIONES SENCILLAS DE UNA SOLA LINEA
triplicar = lambda x: 3 * x
print(triplicar(5))

sumar = lambda x,y: x + y
print(sumar(3,4))

#%%
#MAP PERMITE AFECTAR POR UNA OPERACION A TODOS LOS VALORES DE UNA LISTA 

lista = [1,2,3,4,5]
for i in range(len(lista)):
    lista[i] = lista[i] * 2
    
print(lista)

#PERO LO MISMO Y MEJOR LO PUEDO HACER CON MAP 
#fun es la operacion que se le hara a los valores de la lista 

 #map(func, list)

lista = [1,2,3,4,5,6]
lista = list(map(lambda x: x * 2, lista))
print(lista)

#%%
#FILTER
#NOS PERMITE FILTRAR LOS VALORES DE UNA LISTA 
lista = [1,2,3,4,5,6,7,8,9]
#VAMOS A FILTRAR SOLO LOS NUMEROS PARES
i = 0 
while i < len(lista):
    if lista[i] % 2 != 0:
        lista.pop(i)
    i+=1
    
print(lista)

#AHORA VAMOS HACERLO CON FILTERE
#filter(fun, list)
lista = [1,2,3,4,5,6,7,8,9]
lista = list(filter(lambda x: x % 2 == 0, lista))
print(lista)
#%%
#PAQUETES
#AQUI VAMOS A TENER UNA COLECCION DE FUNCIONEES QUE LAS PODEMOS EXPORTAR ( TODO EN UNA MISMA CARPETA )


#LO VAMOS A VER CON MAYOR CLARIDAD EN EL ARCHIVO fun_calendar

#EN UN ARCHIVO TENDREMOS NUESTRAS FUNCIONES 
#EN OTRO ARCHIVO ESCRIBIMOS NUESTRO ALGORITMO PERO ANTES DE ELLO IMPORTAMOS EL ARCHIVO CON FUNCIONES 