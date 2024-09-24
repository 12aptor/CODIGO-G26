""" Módulos """

# Módulos preinstalados en Python
import os
import sys
import random
import platform
import string
import datetime
import typing


# print(platform.system())

# Módulos creados
import modulo_usuarios
# from modulo_usuarios import mostrarUsuarios, Mascota

print(modulo_usuarios.usuarios)
gato = modulo_usuarios.Mascota()

gato.mostrarNombre()