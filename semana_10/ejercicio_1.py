# -*- coding: utf-8 -*-
class Triangulo:
    def __init__(self, base , altura ):
        self.base = base
        self.altura = altura
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self,val):
        if isinstance(val,int):
            self._base = val
        else:
            raise TypeError("El valor de la base debe ser un numero real")
    
    def area(self):
        return (self.base * self.altura )/2.0
    
    def __repr__(self):
        return f"El area del triangulo es {self.area()}"

# Codigo de prueba de la clase    
T = Triangulo (base = 10, altura = 2)
print(T)
print(T.area())
