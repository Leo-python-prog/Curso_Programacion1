"""
A continuación se presenta un código que intenta representar a una persona, pero invierte el tipo de los campos.

class Persona:
def __init__(self):
self.nombre = 20
self.edad = «»Juan»»

p1 = Persona()
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
p1 = Persona("Juan", 20)
print(f"Nombre: {p1.nombre}, edad: {p1.edad}")