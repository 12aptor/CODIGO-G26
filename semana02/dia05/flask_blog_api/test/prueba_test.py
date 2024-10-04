def suma(a, b):
    return a + b

def resta(a: int, b: int):
    return a - b

def test_suma():
    respuesta = suma(1, 2)
    assert respuesta == 3

def test_resta():
    respuesta = resta(4, 2)
    assert respuesta == 2