from fastapi import FastAPI
from motor import motor_asyncio
from bson.objectid import ObjectId

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.ecommerce
customers_collection = db.customers

app = FastAPI()

@app.get("/")
def home():
    return "Hello World"

@app.get("/customers/list")
async def list_customers():
    customers = customers_collection.find()

    response = []
    for customer in await customers.to_list():
        customer['_id'] = str(customer['_id'])
        response.append(customer)
    return response

@app.get("/customers/create")
async def create_customer():
    customer = await customers_collection.insert_one({
        'name': 'Marcos',
        'age': 50,
    })
    print(customer)
    return "Customer created"

@app.get("/customers/by-id/{customer_id}")
async def get_customer_by_id(customer_id: str):
    customer = await customers_collection.find_one({'_id': ObjectId(customer_id)})
    customer['_id'] = str(customer['_id'])
    return customer