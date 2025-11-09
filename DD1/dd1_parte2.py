import csv
import math

class Triangulo:
    
    def __init__(self, ladoA, ladoB, ladoC):
        
        es_valido = (ladoA > 0 and ladoB > 0 and ladoC > 0) and (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA)
        
        if not es_valido:
            raise ValueError("El triangulo no es valido")
        
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def es_escaleno(self):
        return self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC

    def es_isoceles(self):
        a, b, c = self.ladoA, self.ladoB, self.ladoC
        return (a == b and a != c) or (a == c and a != b) or (b == c and b != a)

    def es_equilatero(self):
        return self.ladoA == self.ladoB == self.ladoC

    def area(self):
        s = (self.ladoA + self.ladoB + self.ladoC) / 2
        return math.sqrt(s * (s - self.ladoA) * (s - self.ladoB) * (s - self.ladoC))

    def __repr__(self):
        return f"Triangulo(ladoA={self.ladoA}, ladoB={self.ladoB}, ladoC={self.ladoC})"

lista_triangulos_validos = []
nombre_archivo = 'triangulos.csv'
total_area = 0.0

try:
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        
        lector_csv = csv.DictReader(archivo)
        
        for fila_dict in lector_csv:
            
            try:
                lado_a_csv = float(fila_dict['LADOA'])
                lado_b_csv = float(fila_dict['LADOB'])
                lado_c_csv = float(fila_dict['LADOC'])
                
                nuevo_triangulo = Triangulo(lado_a_csv, lado_b_csv, lado_c_csv)
                
                lista_triangulos_validos.append(nuevo_triangulo)
                
            except (ValueError, TypeError, KeyError):
                pass
            
except FileNotFoundError:
    print(f"Error fatal: No se encontró el archivo '{nombre_archivo}'")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

if len(lista_triangulos_validos) > 0:
    for idx, t in enumerate(lista_triangulos_validos):
        area_actual = t.area()
        total_area += area_actual
        print(f"{idx}: {t} | Area: {area_actual:.2f}u")
    
    area_promedio = total_area / len(lista_triangulos_validos)
    print(f"\nArea promedio de los triangulos: {area_promedio:.2f}u")
else:
    print("No se encontraron triangulos validos.")