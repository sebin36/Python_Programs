class Item:
    def __init__(self, name, price, description, manufacturer):
        self.name = name
        self.price = price
        self.descript = description
        self.manufact = manufacturer
        self.qty = 1

    def increase_qty(self):
        self.qty += 1
        print('Quantity Increased')

    def decrease_qty(self):
        self.qty -= 1
        print('Quantity Decreased')

    def get_item_details(self):
        print(f'Name: {self.name}, Price: {self.price},\nDescription: {self.descript}, Manufacturer: {self.manufact}')

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print('Item added to the cart.')

    def remove_item(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                print('Item removed from the cart')

    def display_cart(self):
        print('Shopping Cart:')
        for item in self.cart:
            item.get_item_details()


cart = ShoppingCart()

while True:
    print('\nMenu')
    print('1.Add Item to the Cart')
    print('2.Remove Item from Cart')
    print('3.Display Shopping Cart')
    print('4.Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        name = input('Enter Item Name: ')
        price = float(input('Enter Price: Rs.'))
        des = input('Enter Description: ')
        manu = input('Enter Manufacturer: ')
        itm = Item(name,price,des,manu)
        cart.add_item(itm)
    elif choice == 2:
        if not cart.cart:
            print('The cart is empty.')
        else:
            name = input('Enter item to remove: ')
            cart.remove_item(name)
    elif choice == 3:
        if not cart.cart:
            print('The cart is empty.')
        else:
            cart.display_cart()
    elif choice == 4:
        print('Done')
        break
    else:
        print('Invalid Choice')
