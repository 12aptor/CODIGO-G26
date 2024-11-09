from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.ecommerce
customers_collection = db.customers

@app.route('/')
def home():
    return "Hello World!"

@app.route('/customers/list')
def list_customers():
    customers = customers_collection.find().sort({'age': 1})

    response = []
    for customer in customers:
        customer['_id'] = str(customer['_id'])
        response.append(customer)
    return response

@app.get('/customers/create')
def create_customer():
    customer = {
        "name": "John Doe",
        "age": 20,
    }
    customers_collection.insert_one(customer)

    return "Create Customer"

@app.get('/customers/by-id')
def get_customer_by_id():
    id = '672eac2b0800e6a0600d8193'
    customer = customers_collection.find_one({'_id': ObjectId(id)})
    customer['_id'] = str(customer['_id'])
    return customer

if __name__ == '__main__':
    app.run(debug=True)