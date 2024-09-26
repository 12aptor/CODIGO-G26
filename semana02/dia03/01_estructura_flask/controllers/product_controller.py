class ProductController:
    def __init__(self):
        self.products = []

    def create(self, json):
        self.products.append(json)
        return json

    def list(self):
        return self.products
    
    def delete(self, productId):
        updatedProducts = []

        for product in self.products:
            if product['id'] != productId:
                updatedProducts.append(product)
        
        self.products = updatedProducts

        return 'Product deleted'