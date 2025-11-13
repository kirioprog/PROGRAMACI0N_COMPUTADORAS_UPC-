# -*- coding: utf-8 -*-
import math

class Alumno(object):
    # dentro del parentesis con self van a ir los valores que vamos a ingresar para que se ejecute en la clase
    def __init__(self, nombre="", apellido="", codigo="", modalidad="Examen", num_cur=0, n1=0, n2=0, n3=0, n4=0, n5=0):
        # creamos los self y recuerda asignarles un valor
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
        # creamos esta lista para no tener que escribirla a cada rato
        # Si num_cur < 5, rellenamos con 0.0 hasta tener 5 notas
        notas = [n1, n2, n3, n4, n5]
        # Truncar o extender la lista a exactamente 5 elementos
        notas = notas[:5] + [0.0] * (5 - len(notas))
        self.notas = notas

    def promedio(self):
        # Promedio sobre 5 notas
        return sum(self.notas) / 5

    def estaAprobado(self):
        # Criterio: nota > 12.5 cuenta como aprobada. Se requiere al menos 4 notas aprobadas
        aprobado = 0
        for nota in self.notas:
            if nota > 12.5:
                aprobado += 1
        return aprobado >= 4

    def __repr__(self):
        return f"Alumno[nombre={self.nombre}, apellido={self.apellido}, codigo={self.codigo}, modalidad={self.modalidad}, num_cur={self.num_cur}, n1={self.n1}, n2={self.n2}, n3={self.n3}, n4={self.n4}, n5={self.n5}]"


# Codigo de prueba
if __name__ == '__main__':
    a1 = Alumno("Renato", "Sifuentes", 201711069, "Examen", 4, 12, 15, 10, 11)
    a2 = Alumno("Cecilia", "Jimenez", 201508111, "Examen", 5, 10, 12, 12, 13, 14.5)
    a3 = Alumno("Kim", "Wong", 201605010, "TercioSup", 5, 13, 14, 12, 14, 13)
    a4 = Alumno("Juan", "Perez", 201502160, "Nivelacion", 3, 10, 11, 13)
    a5 = Alumno("Sandra", "Arana", 201616020, "Beca", 4, 12, 15, 14, 13)

    lista_alumnos = [a1, a2, a3, a4, a5]

    print("Resultados del ciclo")
    print("--------------------")

    # Barra la lista y muestra: Apellido, Nombre   Codigo: <codigo>  Promedio: XX.X   Aprobado: <S|N>
    for alumno in lista_alumnos:
        prom = alumno.promedio()
        aprobado = 'S' if alumno.estaAprobado() else 'N'
        print(f"Alumno: {alumno.apellido}, {alumno.nombre}   Codigo: {alumno.codigo}  Promedio: {prom:.1f}   Aprobado: {aprobado}")
