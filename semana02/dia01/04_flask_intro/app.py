# Importamos la clase Flask desde el paquete flask
from flask import Flask, request

# Instanciamos la clase Flask
app = Flask(__name__)

# Definimos el endpoint de la aplicación
@app.route('/')
def index():
    return 'Bienvenido a mi app de Flask 😎'

@app.route('/login', methods=['POST', 'GET'])
# @app.route('/sign-in', methods=['POST', 'GET', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def signIn():
    method = request.method

    if method == 'GET':
        return 'Login GET'
    
    elif method == 'POST':
        return 'Login POST'

@app.post('/registro')
def signUp():
    return 'Registro'

@app.get('/usuario/<nombre>')
# @app.get('/usuario/<string:nombre>')
# @app.get('/usuario/<int:id>')
# @app.get('/usuario/<float:price>')
# @app.get('/usuario/<path:subpath>') # /usuario/este/es/un/ejemplo
# @app.get('/usuario/<uuid:uuid>') # /usuario/yu1o3y-1io2u34h-1ph23oa-13j1pj3i
def obtenerUsuario(nombre):
    print(type(nombre))
    return f'Hola {nombre}', 200

@app.get('/html')
def renderHtml():
    return '<button>Dame click!</button>'

@app.post('/ruta-protegida')
def rutaProtegida():
    # Extraer información de los headers
    headers = request.headers
    jwt = headers['Authorization']
    # print(jwt)

    # Recuperar el body
    json = request.json
    print(json)

    return {
        'id': 1,
        'nombre': json['nombre'],
        'precio': json['precio']
    }, 200

# Correr el servidor
if __name__ == '__main__':
    app.run(debug=True)