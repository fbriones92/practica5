from random import randrange
class Trabajo():
    def __init__(self, id, cargo, empresa, sueldo):
        self.id = id
        self.cargo = cargo
        self.empresa = empresa
        self.sueldo = sueldo

class Persona():
    
    MAYORIA_EDAD = 18
    
    def __init__(self, id, nombre, apellido, edad, trabajos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.trabajos = trabajos
        
    def esMayorEdad(self):
        return self.edad >= self.MAYORIA_EDAD
    
    def getSueldoActual(self):
        return randrange(500, 3000)