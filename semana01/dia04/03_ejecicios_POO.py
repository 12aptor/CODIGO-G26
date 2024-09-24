"""Crear un programa que simule el funcionamiento de un cajero automático.
Deberá tener un menú con las siguientes opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar saldo disponible
Iniciar con un saldo de $100"""

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo

    def consultarSaldo(self):
        print(f"Saldo disponible: ${self.saldo}\n")

    def ingresarDinero(self, monto):
        if monto <= 0:
            print("Cantidad no válida")
            return
        
        self.saldo += monto
        print("Depósito realizado")

    def retirarDinero(self, monto):
        if monto <= 0:
            print("Cantidad no válida")
            return
        
        if monto > self.saldo:
            print("Saldo insuficiente")
            return
        
        self.saldo -= monto
        print("Retiro realizado")

def main():
    cajero = Cajero(saldo=100)

    while True:
        print("1. Consultar Saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = int(input("\nIngresa la opción: "))

        if opcion > 3:
            print("Opción no válida")
            # continue: Sirve para que el programa no se detenga y vuelva a ejecutar el bucle
            continue

        if opcion == 1:
            cajero.consultarSaldo()

        elif opcion == 2:
            monto = float(input("\nCuánto desea depositar: "))
            cajero.ingresarDinero(monto)

        elif opcion == 3:
            monto = float(input("\nCuánto desea retirar: "))
            cajero.retirarDinero(monto)

        elif opcion == 4:
            print("Gracias por usar el cajero automático")
            break

main()