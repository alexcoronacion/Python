""" class Person:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

p1=Person("Christian Alexander",39)

print(p1.nombre)
print(p1.edad) """

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self) -> str:
        return f"{self.nombre}({self.edad})"

p1=Persona("christian",39)
print(p1)

