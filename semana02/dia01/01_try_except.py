""" Manejor de excepciones """

# division = 10 / 0

# En el código anterior, se produce un error de división por cero.
# Este error rompe la ejecución del programa.

def main():
    # La finalidad de las excepciones es manejar los errores de forma controlada.
    try:
        # Todo lo que esté dentro de este bloque de código será ejecutado
        # y si se produce un error, se manejará de forma controlada.
        division = 10 / 0
        print("La división se realizó correctamente")

    # En caso de que se produzca un error se ejecutará el bloque except.
    except ZeroDivisionError as error:
        print("En Zero Division Error: ", error)
    except Exception as error:
        print("En Exception: ", error)

    # El bloque finally se ejecutará siempre, independientemente de si se produce un error o no.
    finally:
        print("Try Except finalizado")

# main()

def evaluarEdad(edad):
    try:
        if edad < 18:
            # Lanzar una excepción
            raise Exception("El usuario debe ser mayor de edad")
        
        print("Usuario autorizado")

    except Exception as error:
        print(error)


evaluarEdad(25)