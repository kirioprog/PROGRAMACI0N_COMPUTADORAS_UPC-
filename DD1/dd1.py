import math

class Triangulo:
    
    def __init__(self, ladoA, ladoB, ladoC):
        
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

        es_valido = (self.ladoA + self.ladoB > self.ladoC) and (self.ladoA + self.ladoC > self.ladoB) and (self.ladoB + self.ladoC > self.ladoA)
        
        if not es_valido:
            raise ValueError("El triangulo no es valido")
      
 # ladoA
    @property             
    def ladoA(self):
        return self._ladoA

    @ladoA.setter         
    def ladoA(self, val):

        if (isinstance(val, (int, float))) and val > 0:
            self._ladoA = val
        else:
            raise TypeError("El ladoA debe ser un 'int' o 'float' positivo")

 #lado B
    @property               #
    def ladoB(self):
        return self._ladoB

    @ladoB.setter           
    def ladoB(self, val):
        if (isinstance(val, (int, float))) and val > 0: #
            self._ladoB = val
        else:
            raise TypeError("El ladoB debe ser un 'int' o 'float' positivo") #

 #lado C
    @property               
    def ladoC(self):
        return self._ladoC

    @ladoC.setter           
    def ladoC(self, val):
        if (isinstance(val, (int, float))) and val > 0: #
            self._ladoC = val
        else:
            raise TypeError("El ladoC debe ser un 'int' o 'float' positivo") #

    #metodos
    
    def es_escaleno(self):
    
        return self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC

    def es_isoceles(self):
        
        a, b, c = self.ladoA, self.ladoB, self.ladoC
        return (a == b and a != c) or (a == c and a != b) or (b == c and b != a)

    def es_equilatero(self):
        return self.ladoA == self.ladoB == self.ladoC

    def area(self):
        
        a, b, c = self.ladoA, self.ladoB, self.ladoC
        s = (a + b + c) / 2
        area_calc = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area_calc

    def __repr__(self):
        return f"Triangulo(ladoA={self.ladoA:2}, ladoB={self.ladoB:2}, ladoC={self.ladoC:2})"
    
# CELDA DE PRUEBA DE INSTANCIAMIENTO DE UN TRIANGULO VALIDO (Area: 6u)
t = Triangulo(ladoA=3, ladoB=4, ladoC=5)
print(f"{t} Area: -> {t.area()}u")