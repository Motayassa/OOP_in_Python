class Rect:
    def __init__(self, x, y, width, height):
        self._x = self.check_coord(x)
        self._y = self.check_coord(y)
        self._width = self.check_value(width)
        self._height = self.check_value(height)

    @staticmethod
    def check_coord(coord):
        if type(coord) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        return coord

    @staticmethod
    def check_value(value):
        if value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        return value

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError('sss')

        if not (self._x + self._width < rect._x or
                rect._x + rect._width < self._x or
                self._y + self._height < rect._y or
                rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False

lst_rect = [Rect(0, 0, 5, 3),
            Rect(6, 0, 3, 5),
            Rect(3, 2, 4, 4),
            Rect(0, 8, 8, 1)]

lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                     if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]


r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
