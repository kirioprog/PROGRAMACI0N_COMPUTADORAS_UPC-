class CircuitoResistivo:
    
    # Inicializacion
    def __init__(self, resistencias=[]):
        #estamos llamando a la lista resisnteica como self. resistencia
        #asi que en todas nuetras operacioones llamamos self.resistencia si queremos utilizar la lista 
        self.resistencia = resistencias
        
    def calculaEquivalenteSerie(self):
        cont = 0
        for idx in self.resistencia:
            cont += idx
        return cont
            
        

    def calculaEquivalenteParalelo(self):
        cont = 0 
        for idx in self.resistencia:
            cont += 1/idx
        return cont
        

# Prueba 
c1 = CircuitoResistivo([120, 450, 345, 1000, 780, 1300])
res = c1.calculaEquivalenteSerie()
rep = c1.calculaEquivalenteParalelo()
print("La resistencia equivalente en serie es", res)
print(f"La resistencia equivalente en paralelo es {rep:.3f}")