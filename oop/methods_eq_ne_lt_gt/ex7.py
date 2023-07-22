class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @staticmethod
    def mass(ro, volume):
        return ro * volume

    def __gt__(self, other):
        if type(other) == Body and type(self) == Body:
            body1 = self.mass(self.ro, self.volume)
            body2 = self.mass(other.ro, other.volume)
            return body1 > body2

        if type(self) == Body and type(other) in (int, float):
            body2 = self.mass(self.ro, self.volume)
            return body2 > other

    def __rgt__(self, other):
        return self > other

    def __lt__(self, other):
        if type(other) in (int, float) and type(self) == Body:
            body1 = self.mass(self.ro, self.volume)
            return body1 < other
        if type(self) == Body and type(other) == Body:
            body1 = self.mass(self.ro, self.volume)
            body2 = self.mass(other.ro, other.volume)
            return body1 < body2

    def __eq__(self, other):
        if type(other) == Body and type(self) == Body:
            body1 = self.mass(self.ro, self.volume)
            body2 = self.mass(other.ro, other.volume)
            return body1 == body2
        if type(other) in (int, float) and type(self) == Body:
            body2 = self.mass(self.ro, self.volume)
            return body2 == other


a = Body('Lora', 10, 10)
b = Body('Dora', 20, 20)
assert hasattr(a, "name") and hasattr(a, "ro") and hasattr(a, "volume"), "ошибка в локальных атрибутах"
assert type(a.name) is str, "name может быть только строкой"
assert type(a.ro) in (int, float), "ro  должно быть int или float"
assert type(a.volume) in (int, float), "volume  должно быть int или float"
assert not a > b, "ошибка при сравнении объектов >"
assert a < b, "ошибка при сравнении объектов <"
assert 10 < a, "ошибка при сравнении число < объект"
assert not 10 > a, "ошибка при сравнении число > объект"
assert not a == 5, "ошибка при сравнении объект == число"
assert a != 5, "ошибка при сравнении объект != число"
print("Правильное решение.")
