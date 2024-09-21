"""Programación Orientada a objetos"""

class Persona:
    # Constructor
    def __init__(self, nombre, edad, estadoCivil, vivo):
        self.nombre = nombre
        self.edad = edad
        self.estadoCivil = estadoCivil
        self.vivo = vivo

    # Métodos
    def saludar(self):
        # Un método privado se puede llamar desde el mismo objeto
        # print(self.__estaVivo())
        print("Hola que tal!")

    def presentar(self):
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años"
    
    # Métodos privados
    def __estaVivo(self):
        if self.vivo:
            return "Estoy vivo"
        
        return "Estoy con San Pedro"


# Instanciar la clase
pepito = Persona(nombre="Pepito", edad=40, estadoCivil="CASADO", vivo=True)

# Accedemos a los atributos
print(pepito.estadoCivil)

# Accedemos a un método
pepito.saludar()
print(pepito.presentar())

jhon = Persona(nombre="Jhon", edad=30, estadoCivil="SOLTERO", vivo=True)
print(jhon.estadoCivil)
print(jhon.presentar())

# No se puede acceder a un método privado fuera del mismo objeto
# print(jhon.__estaVivo())


"""Herencia"""
class Alumno(Persona):

    def mostrarEdad(self):
        print(f"Soy {self.nombre} y mi edad es {self.edad}")


alumnaMaria = Alumno(nombre="Maria", edad=30, estadoCivil="SOLTERA", vivo=True)
alumnaMaria.mostrarEdad()