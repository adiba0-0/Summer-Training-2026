from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, price):
        self.__product_id = product_id
        self.__price = price

    def get_price(self):
        return self.__price

    def get_product_id(self):
        return self.__product_id

    @abstractmethod
    def final_price(self):
        pass


class Electronics(Product):
    def final_price(self):
        discount = self.get_price() * 0.10
        print("Electronics")
        print("Product ID:", self.get_product_id())
        print("Final Price:", self.get_price() - discount)


class Clothing(Product):
    def final_price(self):
        discount = self.get_price() * 0.20
        print("Clothing")
        print("Product ID:", self.get_product_id())
        print("Final Price:", self.get_price() - discount)


class Grocery(Product):
    def final_price(self):
        discount = self.get_price() * 0.05
        print("Grocery")
        print("Product ID:", self.get_product_id())
        print("Final Price:", self.get_price() - discount)


products = [
    Electronics(101, 50000),
    Clothing(102, 2000),
    Grocery(103, 500)
]

for item in products:
    item.final_price()
    print()