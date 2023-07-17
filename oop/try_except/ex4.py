class Triangle:
    def __init__(self, a, b, c):
        self._a = self.__check_value(a)
        self._b = self.__check_value(b)
        self._c = self.__check_value(c)
        self.__check_triangle()

    @staticmethod
    def __check_value(value):
        if type(value) not in (int, float):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        return value

    def __check_triangle(self):
        if self._a > self._b + self._c or self._b > self._a + self._c or self._c > self._a + self._b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for data in input_data:
    try:
        obj = Triangle(*data)
        lst_tr.append(obj)
    except TypeError:
        pass
    except ValueError:
        pass
print(lst_tr)
