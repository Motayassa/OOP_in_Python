class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    count_id = 0
    attrs = {'id': [int],
             'name': [str],
             'weight': [int, float],
             'price': [int, float]
             }

    def __new__(cls, *args, **kwargs):
        cls.count_id += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.count_id

    def __setattr__(self, key, value):
        if type(value) in (int, float) and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in self.attrs and type(value) in self.attrs[key]:
            return super.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            return super.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
