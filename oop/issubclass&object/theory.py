'''___________________Функция issubclass() от object____________________'''


class Geom(object):  # эквивалент class Geom:
    pass


class Line(Geom):
    pass


print(Geom.__class__)
g = Geom()
print(g)
l = Line()
print(l.__class__)
#  является ли тот или иной класс подклассом другого класса
print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
#  проверить принадлежность объекта тому или иному классу, или базовому
print(isinstance(l, Geom))
print(isinstance(l, Line))
print(isinstance(l, object))


'''______________Наследование от встроенных типов данных__________________'''


issubclass(int, object)
issubclass(list, object)


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
print(type(v))
