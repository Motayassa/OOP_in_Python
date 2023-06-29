class Vector:
    def __init__(self, *args, **kwargs):
        self.coords = list(args)

    def __len__(self):
        return len(self.coords)

    def check(self, v1, v2):
        if len(v1) != len(v2):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if self.check(self, other):
            res = [x + y for x, y in zip(self.coords, other.coords)]
            return self.__class__(*res)

    def __iadd__(self, other):
        if type(other) in (int, float):
            for i, j in enumerate(self.coords):
                self.coords[i] += other
            return self
        if type(other) == self.__class__:
            for i, j in enumerate(self.coords):
                self.coords[i] += other.coords[i]
            return self

    def __sub__(self, other):
        if self.check(self, other):
            res = [x - y for x, y in zip(self.coords, other.coords)]
            return self.__class__(*res)

    def __isub__(self, other):
        if type(other) in (int, float):
            for i, j in enumerate(self.coords):
                self.coords[i] -= other
            return self
        if type(other) == self.__class__:
            for i, j in enumerate(self.coords):
                self.coords[i] -= other.coords[i]
            return self

    def __mul__(self, other):
        if self.check(self, other):
            res = [x * y for x, y in zip(self.coords, other.coords)]
            return self.__class__(*res)

    def __eq__(self, other):
        if len(self.coords) > len(other.coords):
            x = self.coords[:len(other.coords)]
            y = other.coords
        if len(self.coords) < len(other.coords):
            x = self.coords
            y = other.coords[:len(self.coords)]
        if len(self.coords) == len(other.coords):
            x = self.coords
            y = other.coords

        for i, j in enumerate(x):
            if j != y[i]:
                return False
        return True

    def __ne__(self, other):
        if len(self.coords) > len(other.coords):
            x = self.coords[:len(other.coords)]
            y = other.coords
        if len(self.coords) < len(other.coords):
            x = self.coords
            y = other.coords[:len(self.coords)]
        if len(self.coords) == len(other.coords):
            x = self.coords
            y = other.coords

        for i, j in enumerate(x):
            if j != y[i]:
                return True
        return False


# TEST-TASK___________________________________
v1 = Vector(1, 1, 1, 1)
v2 = Vector(1, 2, 3, 4)
# При реализации бинарных операторов +, -, *
# следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. 
v3 = v1 + v2
assert list(*v3.__dict__.values()) == [2, 3, 4, 5], \
       "ошибка предпологается что в объекте будет только 1 локальный атрибут с координатами"
assert id(v3) != id(v1) and id(v3) != id(v2), "ошибка, при + должен создаваться новый объект"

v4 = v1 - v2
assert list(*v4.__dict__.values()) == [0, -1, -2, -3], \
       "ошибка предпологается что в объекте будет только 1 локальный атрибут с координатами"
assert id(v4) != id(v1) and id(v4) != id(v2), "ошибка, при - должен создаваться новый объект"

v5 = v1 * v2
assert list(*v4.__dict__.values()) == [0, -1, -2, -3], \
       "ошибка предпологается что в объекте будет только 1 локальный атрибут с координатами"
assert id(v5) != id(v1) and id(v5) != id(v2), "ошибка, при * должен создаваться новый объект"

# При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
temp = id(v1)
v1 += 10
assert id(v1) == temp and list(*v1.__dict__.values()) == [11, 11, 11, 11], \
       "ошибка, при v1 += 10 объект должен оставаться прежним, не нужно создавать новый объект"

v1 += v5
assert id(v1) == temp and list(*v1.__dict__.values()) == [12, 13, 14, 15], \
       "ошибка, при v1 += v5 объект должен оставаться прежним, не нужно создавать новый объект"

v1 -= v5
assert id(v1) == temp and list(*v1.__dict__.values()) == [11, 11, 11, 11], \
       "ошибка, при v1 -= v5 объект должен оставаться прежним, не нужно создавать новый объект"

v1 -= 10
assert id(v1) == temp and list(*v1.__dict__.values()) == [1, 1, 1, 1], \
       "ошибка, при v1 -= 10 объект должен оставаться прежним, не нужно создавать новый объект"

v11 = Vector(1, 1, 1, 1)
v22 = Vector(1, 1, 1, 1)
ans = v11 == v22  # True
assert ans, "ошибка, v1 == v2 # True, если соответствующие координаты векторов равны"
ans1 = v1 != v2  # True
assert ans1, "ошибка, v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает"

# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, *
# должно генерироваться исключение командой:
# raise ArithmeticError('размерности векторов не совпадают')
x1 = Vector(1, 1, 1)
x2 = Vector(1, 1, 1, 1)
try:
    x1 + x2
except ArithmeticError:
    assert True
else:
    assert False, "ошибка, не сгенерировалась ошибка ArithmeticError при операции x1 + x2"

try:
    x1 - x2
except ArithmeticError:
    assert True
else:
    assert False, "ошибка, не сгенерировалась ошибка ArithmeticError при операции x1 - x2"
    
try:
    x1 * x2
except ArithmeticError:
    assert True
else:
    assert False, "ошибка, не сгенерировалась ошибка ArithmeticError при операции x1 * x2"

print("Правилно, так держать !")