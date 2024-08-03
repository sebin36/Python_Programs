class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_description(self):
        pass

class Electronics(Product):
    def __init__(self, product_id, name, price, manufacturer):
        super().__init__(product_id, name, price)
        self.manufacturer = manufacturer

    def get_description(self):
        return f'{self.name}(by {self.manufacturer}) - Price:${self.price}'

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def get_description(self):
        return f'{self.name}(Size:{self.size}) - Price:${self.price}'

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def update_product(self, product_id, new_price):
        available = False
        for prod in self.inventory:
            if prod.product_id == product_id:
                available = True
                prod.price = new_price

        if not available:
            print('Product not Found')

    def display_inventory(self):
        for prod in self.inventory:
            print(prod.get_description())

electro1 = Electronics('E001','Laptop',800,'Dell')         
electro2 = Electronics('E02','Smartphone',600,'Asus')
cloth1 = Clothing(1,'T-shirt',120,'M')
cloth2 = Clothing(2,'Jeans',150,'L')

inventory = Inventory()

inventory.add_product(electro1)
inventory.add_product(cloth2)
inventory.add_product(electro2)
inventory.add_product(cloth1)

inventory.update_product('E001',1000)
inventory.update_product(2, 25)

inventory.display_inventory()

                
