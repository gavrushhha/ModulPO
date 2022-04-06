from typing import List
class Product():
    name: str
    price:  float
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Basket():
    basket: List[Product] = []
    def add(self, product: Product):
        self.basket.append(product)
        return self.basket
    def remove(self, product: Product):
        self.basket.remove(product)
        return self.basket
    def count_sum(self, price: Product):
        for price in self.basket:
            summa = sum(price)
            return summa
