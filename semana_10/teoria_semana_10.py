# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
# =============================================================================
# ARCHIVO: figuras.py
# =============================================================================
# Este archivo define la clase 'Circulo'.
# Está pensado para que otros scripts lo puedan importar y usar.
# Por ejemplo: from figuras import Circulo
# %%

class Circulo:
    """
    ¡Un molde para crear objetos Círculo! 🔵
    
    Básicamente, define un círculo usando dos cosas clave:
    1. Su radio (qué tan grande es).
    2. Su origen (dónde está su centro en un plano 2D, como (x, y)).
    """
    
    def __init__(self, radio=1, origen=(0, 0)):
        """
        El "constructor" (método mágico __init__). Se llama SÍ O SÍ
        automáticamente cuando creas un nuevo círculo (ej: c1 = Circulo()).
        
        Es como la "lista de ensamblaje" de la fábrica de círculos:
        "Toma el radio y el origen que me dan (o usa los valores por defecto)
        y asígnalos al nuevo objeto que estoy construyendo".
        
        Atributos (los que recibe):
            - radio (int o float): El tamaño del radio. Por defecto es 1.
            - origen (tupla): Una tupla (x, y) para el centro. Por defecto es (0, 0).
        """
        # Ojo aquí: Cuando asignamos 'self.radio = radio', Python es
        # lo suficientemente listo como para NO guardar el valor directamente.
        # En su lugar, ¡llama al método "setter" que definimos más abajo
        # con el decorador @radio.setter!
        self.radio = radio
        self.origen = origen
        
    def area(self):
        """
        Calcula y devuelve el área del círculo.
        La fórmula es: PI * radio^2
        
        Uso:
            mi_circulo.area()
        """
        # Usamos 3.1415 como una aproximación de PI
        return 3.1415 * self.radio ** 2
    
    def perimetro(self):
        """
        Calcula y devuelve el perímetro (la circunferencia).
        La fórmula es: 2 * PI * radio
        
        Uso:
            mi_circulo.perimetro()
        """
        return 2 * 3.1415 * self.radio

    # %%
    # =============================================================================
    # GETTERS Y SETTERS (¡La forma "Pythonica" de controlar atributos!)
    # =============================================================================
    
    # --- GETTER para Radio ---
    @property
    def radio(self):
        """
        Este es el GETTER para 'radio'.
        Un "getter" es un método que se disfraza de atributo.
        
        Le dice a Python: "Cuando alguien intente LEER el valor de 'obj.radio'..."
        ...tú en realidad ejecuta este código y devuelve el valor 
        que está guardado en 'self._radio' (con guion bajo).
        
        Uso (lectura):
            print(mi_circulo.radio)
        """
        return self._radio
    
    # --- GETTER para Origen ---
    @property
    def origen(self):
        """
        Este es el GETTER para 'origen'.
        Funciona igual que el getter de radio.
        
        Permite LEER el valor "privado" 'self._origen'.
        
        Uso (lectura):
            print(mi_circulo.origen)
        """
        return self._origen
    
    # --- SETTER para Radio ---
    @radio.setter
    def radio(self, val):
        """
        Este es el SETTER para 'radio'.
        Le dice a Python: "Cuando alguien intente ASIGNAR un valor
        (ej: mi_circulo.radio = 10)..."
        
        "...¡NO lo guardes todavía! Primero, ejecuta este código de validación".
        Es como un guardia de seguridad para tus atributos.
        
        Regla: El radio DEBE ser un número (int o float) Y mayor que 0.
        """
        if (isinstance(val, int) or isinstance(val, float)) and val > 0:
            # Si el valor (val) es un número Y es positivo... ¡Adelante!
            # Guardamos el valor en el atributo "privado" self._radio
            self._radio = val
        else:
            # Si no cumple, ¡lanzamos un error! No dejamos que pongan datos malos.
            raise TypeError("La propiedad 'radio' debe ser un 'int' o 'float' mayor que 0")
            
    # --- SETTER para Origen ---
    @origen.setter
    def origen(self, val):
        """
        Este es el SETTER para 'origen'.
        Se activa cuando haces: obj.origen = (10, 20)
        
        Reglas:
        1. Debe ser una tupla.
        2. Los dos elementos de la tupla deben ser números (int o float).
        """
        if isinstance(val, tuple):
            # Ok, es una tupla. Ahora miremos adentro...
            if isinstance(val[0], int) or isinstance(val[0], float) and isinstance(val[1], int) or isinstance(val[1], float):
                # ¡Perfecto! Ambos son números. Lo guardamos en self._origen
                self._origen = val
            else:
                # La tupla no tiene números adentro.
                raise TypeError("Las coordandas de 'origen' debe ser numéricas")
        else:
            # Ni siquiera es una tupla.
            raise TypeError("La propiedad 'origen' debe ser una 'tuple'")

    # %%
    # =============================================================================
    # MÉTODOS DE INSTANCIA (Acciones que el Círculo puede hacer)
    # =============================================================================
            
    def mover_derecha(self, paso):
        """Mueve el círculo a la derecha sumando al eje X."""
        if isinstance(paso, int) or isinstance(paso, float):
            # Actualizamos el origen.
            # OJO: ¡Esto llama automáticamente al SETTER de 'origen'!
            # El setter validará que la nueva tupla (x, y) sea correcta (y lo es).
            self.origen = (self.origen[0] + paso, self.origen[1])
        else:
            raise TypeError("El paso debe ser numerico")
    
    def mover_izquierda(self, paso):
        """Mueve el círculo a la izquierda restando al eje X."""
        if isinstance(paso, int) or isinstance(paso, float):
            self.origen = (self.origen[0] - paso, self.origen[1])
        else:
            raise TypeError("El paso debe ser numerico")
    
    def mover_arriba(self, paso):
        """Mueve el círculo hacia arriba sumando al eje Y."""
        if isinstance(paso, int) or isinstance(paso, float):
            self.origen = (self.origen[0], self.origen[1] + paso)
        else:
            raise TypeError("El paso debe ser numerico")
    
    def mover_abajo(self, paso):
        """Mueve el círculo hacia abajo restando al eje Y."""
        if isinstance(paso, int) or isinstance(paso, float):
            self.origen = (self.origen[0], self.origen[1]- paso)
        else:
            raise TypeError("El paso debe ser numerico")
            
    def expandir(self, paso):
        """Aumenta el radio del círculo."""
        if isinstance(paso, int) or isinstance(paso, float):
            # Esto también llama al SETTER de 'radio'.
            # El setter validará que el nuevo radio (radio + paso)
            # siga siendo positivo.
            self.radio += paso
        else:
            raise TypeError("El paso debe ser numerico")
    
    def contraer(self, paso):
        """
        Reduce el radio del círculo, con un control extra.
        """
        if isinstance(paso, int) or isinstance(paso, float):
            # Aquí SÍ necesitamos chequear ANTES de asignar.
            # ¿Por qué? Si radio=5 y paso=10, self.radio -= paso
            # intentaría asignar -5. El setter @radio.setter lo
            # detectaría y lanzaría TypeError.
            # Pero queremos un error más específico (ValueError)
            # que indique que la *operación* es inválida.
            if self.radio - paso > 0:
                self.radio -= paso
            else:
                # Error personalizado ANTES de que el setter falle.
                raise ValueError("El paso no debe de generar un radio negativo")
        else:
            raise TypeError("El paso debe der numerico")
            
    def esta_dentro(self, x, y):
        """
        Verifica si un punto (x, y) está dentro del círculo (incluido el borde).
        
        Usa la ecuación de la circunferencia:
        Si (x - h)^2 + (y - k)^2 <= r^2, el punto está dentro.
        Donde (h, k) es el origen (self.origen) y r es el radio.
        """
        return (x - self.origen[0])**2 + (y - self.origen[1])**2 <= self.radio ** 2
        
    def __repr__(self):
        """
        Método mágico 'repr' (Representación).
        Define cómo se "imprime" el objeto cuando haces print(obj)
        o simplemente escribes 'obj' en una consola.
        
        ¡Súper útil para debugging y para ver qué tienes!
        """
        # Devolvemos un string formateado que muestra el estado actual
        return "Circulo[radio={}, origen={}]".format(self.radio, self.origen)
 
# %%
# =============================================================================
# PUNTO DE ENTRADA (Si ejecutas este archivo: python figuras.py)
# =============================================================================

def main():
    """
    Función principal.
    
    Se deja 'pass' (no hacer nada) aquí porque este archivo (figuras.py)
    está pensado principalmente para ser IMPORTADO por otro script,
    no para ser ejecutado por sí mismo.
    
    Si quisieras probar la clase, pondrías tu código de prueba aquí,
    (como los 'c1 = Circulo(...)' o los 'try...except' que vimos
    en el notebook).
    """
    pass

# Esta es la convención estándar de Python.
# Le pregunta al intérprete:
# "¿Alguien está ejecutando este archivo .py directamente?"
# (Ej: corriendo 'python figuras.py' en la terminal)
#
# Si __name__ es '__main__', la respuesta es SÍ.
if __name__ == '__main__':
    # ...entonces ejecuta la función main().
    main()

# Si la respuesta es NO (o sea, alguien hizo 'import figuras' desde
# otro script), el __name__ será 'figuras' y este bloque NO se ejecuta.
# (Lo cual es bueno, ¡no queremos que corra código de prueba
# solo por importar la clase!)