class Furniture:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self.__verify_name(value):
            self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if self.__verify_weight(value):
            self._weight = value

    def __verify_name(self, value):
        if type(value) != str:
            raise TypeError('название должно быть строкой')
        return True

    def __verify_weight(self, value):
        if type(value) not in (int, float):
            raise TypeError('вес должен быть положительным числом')
        if value <= 0:
            raise TypeError('вес должен быть положительным числом')
        return True

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('hh', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(cl.get_attrs())
