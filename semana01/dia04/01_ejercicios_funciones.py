"""Crear un juego de adivinanza de números. El programa debe
generar un número aleatorio entre 1 - 10 y el programa debe ayudarte
con ES MENOR y ES MAYOR"""

import random

def adivinar():
    numeroAleatorio = random.randint(1, 10)
    intentos = 0
    print("!Bienvenido! Estoy pensando en un número entre 1 y 10. ¿Sabes cuál es el número?")

    while True:
        respuesta = int(input("Adivina el número: "))
        intentos += 1
        
        if respuesta == numeroAleatorio:
            print(f"!Felicidades! Has adivinado el número en el intento {intentos}")
            break
        elif respuesta < numeroAleatorio:
            print("El número ES MAYOR")
        else:
            print("El número ES MENOR")

# adivinar()


"""Crear un programa que genere contraseñas seguras. El programa debe
pedir al usuario la longitud de la contraseña"""

import string

def generarPassword():
    longitud = int(input("Número de caracteres de la contraseña: "))
    # caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    print(f"Tu contraseña segura es: {password}")
        
# generarPassword()

import requests

"""Crear un programa que muestre posts.
Consumiendo la siguiente api: https://jsonplaceholder.typicode.com/posts/1"""

# pip install requests

def mostrarPost():
    API_URL = "https://jsonplaceholder.typicode.com/posts/1"
    respuesta = requests.get(API_URL)
    datos = respuesta.json()
    # {
    #     'userId': 1,
    #     'id': 1,
    #     'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
    #     'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
    # }
    print(datos)
    print(f"Título: {datos['title']}")
    print(f"Contenido: {datos['body']}")

mostrarPost()