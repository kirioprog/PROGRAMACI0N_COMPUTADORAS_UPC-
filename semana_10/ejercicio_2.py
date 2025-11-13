# -*- coding: utf-8 -*-
class Capacitor:
    # Inicializacion
    def __init__(self, valor = 0):
        self.valor = valor
    #importante el getter o property
    @property
    def valor(self):
        return self._valor
    
    #Filtramos el valor de self.valor/ casi siempre es la misma estructura 
    @valor.setter
    def valor(self,val):
        if (isinstance(val, float) and val > 0 ):
            self._valor = val
        else:
            raise TypeError("El valor debe ser un numero y mayor a cero")
    #Capacitores en paralelo
    def __add__(self, other):
        return Capacitor(self.valor + other.valor)
    #capacitores en serie 
    def __floordiv__(self, other):
        #todo Ponemos other.valor para poder acceder al valor del capacitor , es como si hubiesen 2 capacitores el capacitor self y el capacitor other 
        return Capacitor(1/(1/other.valor + 1/self.valor))
    
    def __repr__(self):
        return f"El valor de la Resistencia equivalente es {self.valor}"

# Prueba (tres resistencias de 1kOhm)
c1 = Capacitor(1e-6)
c2 = Capacitor(1e-6)
c3 = Capacitor(1e-6)

result = c1 + (c2 // c3)
print(result.valor)