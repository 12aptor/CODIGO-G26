# Importamos la clase Flask desde el paquete flask
from flask import Flask

# Instanciamos la clase Flask
app = Flask(__name__)

# Definimos el endpoint de la aplicación
@app.route('/')
def index():
    return 'Bienvenido a mi app de Flask 😎'

# Correr el servidor
if __name__ == '__main__':
    app.run(debug=True)