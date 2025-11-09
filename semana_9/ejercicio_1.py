class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __repr__(self):
        return (f"La base del triangulo es {self.base}  y  su altura es {self.altura} ")

    
    def perimetro(self):
        return self.base + 2*self.altura
            
    
    def area(self):
        return (self.base * self.altura )/2



# Codigo de prueba de la clase    
R = Rectangulo(base = 10, altura = 2)
print(R.area())
print(R.perimetro())