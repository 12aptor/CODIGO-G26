from flask import Flask, request
from controllers.product_controller import ProductController


app = Flask(__name__)

controller = ProductController()

@app.get('/')
def index():
    return 'Hello Flask 🤠'


@app.post('/product/create')
def createProduct():
    json = request.get_json()
    return controller.create(json)

@app.get('/product/list')
def listProducts():
    return controller.list()

@app.delete('/product/delete/<int:productId>')
def deleteProduct(productId):
    return controller.delete(productId)

if __name__ == '__main__':
    app.run(debug=True)