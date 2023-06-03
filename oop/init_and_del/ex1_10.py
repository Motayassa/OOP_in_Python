class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{x.name}: {x.price}" for x in self.goods]


def create_product(self, name, price):
    self.name = name
    self.price = price


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('LG', 5000))
cart.add(Table('Ikea', 343))
cart.add(Notebook('Apple', 12000))
cart.add(Notebook('Apple', 7800))
cart.add(Cup('{a[', 10))
