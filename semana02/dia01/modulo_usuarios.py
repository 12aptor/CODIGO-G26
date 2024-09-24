usuarios = ["admin", "pepe", "juan"]

def mostrarUsuarios():
    for usuario in usuarios:
        print(usuario)


class Mascota:
    def __init__(self):
        self.nombre = "Firulais"

    def mostrarNombre(self):
        print(f"La mascota se llama: {self.nombre}")