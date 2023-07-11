class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    count_id = 0

    def __new__(cls, *args, **kwargs):
        cls.count_id += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.__id = self.count_id
        self._name = name
        self._weight = weight
        self._price = price

    def get_id(self):
        return self.__id


ShopItem(' ', 12, 100)