class Vector:
    _allowed_types = (int, float)

    def __init__(self, *args):
        self.__check_coords(args)
        self.args = args

    def __check_coords(self, args):
        if not all(type(x) in self._allowed_types for x in args):
            raise ValueError('Неверный тип координат')

    def __check_len(self, x, y):
        if len(x) != len(y):
            raise TypeError('размерности векторов не совпадают')

    def __len__(self):
        return len(self.args)

    def __make_vector(self, sum_lst):
        try:
            return self.__class__(*sum_lst)
        except ValueError:
            return Vector(sum_lst)

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_len(self, other)
        sum_lst = map(lambda x, y: x + y, self.args, other.args)
        return self.__make_vector(sum_lst)

    @staticmethod
    def __is_vector(obj):
        if not isinstance(obj, Vector):
            raise TypeError('оператор должен быть объектом класса Вектор или любого дочернего от него Вектора')

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_len(self, other)
        sub_lst = list(map(lambda x, y: x - y, self.args, other.args))
        return self.__class__(*sub_lst)

    def get_coords(self):
        return tuple(self.args)


class VectorInt(Vector):
    _allowed_types = (int,)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

    
v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1+v2
assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1+v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
 