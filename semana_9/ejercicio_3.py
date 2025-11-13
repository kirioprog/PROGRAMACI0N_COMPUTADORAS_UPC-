# -*- coding: utf-8 -*-
import math
class Alumno(object):
     # dentro del parentesis con self van a ir los valores que vamos a ingresar par que se ejecuta en la clase, los valores que luego le demos a la clase tienen que etar en el mismo orden 
    def __init__(self, nombre="", apellido="", codigo="", modalidad="Examen", num_cur=0, n1=0, n2=0, n3=0, n4=0, n5=0):
        #creamos los self y recuerda asignarles un valor 
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.modalidad = modalidad
        self.num_cur = num_cur
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        #creamos esta lista para no tener que escribirla a cada rato 
        self.notas = [n1, n2, n3, n4, n5]

    
    def promedio(self):
        
        prom = sum(self.notas) / 5
        return prom

            
            
            
    def estaAprobado(self):
        aprobado = 0
        for idx, nota in enumerate(self.notas, start = 0):
            if nota > 12.5:
                aprobado +=1
        
        if aprobado >= 4:
            return True
        else:
            return False
        

    def __repr__(self):
        return f"Alumno[nombre={self.nombre}, apellido={self.apellido}, codigo={self.codigo}, modalidad={self.modalidad}, num_cur={self.num_cur}, n1={self.n1}, n2={self.n2}, n3={self.n3}, n4={self.n4}, n5={self.n5}]"



# Codigo de prueba
a1 = Alumno("Renato", "Sifuentes", 201711069, "Examen", 4, 12, 15, 10, 11)
a2 = Alumno("Cecilia", "Jimenez", 201508111, "Examen", 5, 10, 12, 12, 13, 14.5)
a3 = Alumno("Kim", "Wong", 201605010, "TercioSup", 5, 13, 14, 12, 14, 13)
a4 = Alumno("Juan", "Perez", 201502160, "Nivelacion", 3, 10, 11, 13)
a5 = Alumno("Sandra", "Arana", 201616020, "Beca", 4, 12, 15, 14, 13)

#print("Objetos creados")
#print("---------------")
#print(a1, "\n")
#print(a2, "\n")
#print(a3, "\n")
#print(a4, "\n")
#print(a5, "\n")
#print()

lista_alumnos = [a1, a2, a3, a4, a5]

print("Resultados del ciclo")
print("--------------------\n")

for alumno in lista_alumnos:
    prom = alumno.promedio()
    aprobado = 'S' if alumno.estaAprobado() else 'N'
    print(f"Alumno: {alumno.apellido}, {alumno.nombre}   Codigo: {alumno.codigo}  Promedio: {prom:.1f}   Aprobado: {aprobado}")
    print()
# Insertar un codigo que barra la lista_alumnos y retorne la siguiente impresion:
# Alumno: <Apellido>, <Nombre>   Codigo: <codigo>  Promedio: XX.X   Aprobado: <S|N>