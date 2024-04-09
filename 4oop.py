from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def product_type(self):
        pass

    def get_price(self):
        return self._price



class Dress(Product):
    def product_type(self):
        return "Dress"

class TShirt(Product):
    def product_type(self):
        return "T-Shirt"

class Skirt(Product):
    def product_type(self):
        return "Skirt"

class Sweater(Product):
    def product_type(self):
        return "Sweater"



class LipStick(Product):
    def product_type(self):
        return "LipStick"

class LipGloss(Product):
    def product_type(self):
        return "LipGloss"

class Blush(Product):
    def product_type(self):
        return "Blush"

class Mascara(Product):
    def product_type(self):
        return "Mascara"



class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_cost(self):
        return sum(product.get_price() for product in self.products)

    def display_products(self):
        for product in self.products:
            print(f"{product.product_type()}: {product._name} - ${product.get_price()}")



CLOTHING_CATALOG = {
    "dress": Dress("Dress", 49.99),
    "t-shirt": TShirt("T-Shirt", 19.99),
    "skirt": Skirt("Skirt", 39.99),
    "sweater": Sweater("Sweater", 59.99)
}

MAKEUP_CATALOG = {
    "lipstick": LipStick("LipStick", 14.99),
    "lipgloss": LipGloss("LipGloss", 9.99),
    "blush": Blush("Blush", 19.99),
    "mascara": Mascara("Mascara", 12.99)
}


def user_interaction():
    cart = ShoppingCart()
    print("Welcome to our Online Shop!")
    while True:
        category = input("Choose a category (Clothing/MakeUp) or 'done' to finish: ").lower()
        if category == "done":
            break

        if category == "clothing":
            item = input("Choose an item (Dress, T-Shirt, Skirt, Sweater): ").lower()
            product = CLOTHING_CATALOG.get(item)
        elif category == "makeup":
            item = input("Choose an item (LipStick, LipGloss, Blush, Mascara): ").lower()
            product = MAKEUP_CATALOG.get(item)
        else:
            print("Invalid category. Please choose again.")
            continue

        if product:
            cart.add_product(product)
            print(f"{product.product_type()} added to cart.")
        else:
            print("Invalid item. Please choose again.")

    cart.display_products()
    print(f"Total Cost: ${cart.total_cost()}")

user_interaction()

#HOW ARE THE 4OOP's FOUND IN THIS CODE:
#Encapsulation: Attributes are kept private within the Product class and accessed via methods.
#Inheritance: Dress, TShirt, Skirt, Sweater, LipStick, LipGloss, Blush, and Mascara classes are inherited from Product.
#Abstraction: The Product class is abstract and defines the abstract method product_type.
#Polymorphism: Each subclass provides its own implementation of the product_type method.

#Sources:
#https://www.geeksforgeeks.org/encapsulation-in-python/
#https://www.geeksforgeeks.org/inheritance-in-python/
#https://www.mygreatlearning.com/blog/abstraction-in-python/
#https://www.geeksforgeeks.org/data-abstraction-in-python/
#https://www.geeksforgeeks.org/polymorphism-in-python/