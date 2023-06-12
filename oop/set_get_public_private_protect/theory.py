'''attribute (без одного или двух подчеркиваний вначале)
– публичное свойство (public);
_attribute (с одним подчеркиванием) –
режим доступа protected (служит для обращения внутри класса и
во всех его дочерних классах)
__attribute (с двумя подчеркиваниями) –
режим доступа private (служит для обращения только внутри класса).
'''

from accessify import private  # protected


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0

        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_сoord(self):
        return self.__x, self.__y

    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)


pt = Point(1, 2)
pt.set_coord(1, 2)
print(pt.get_сoord())
print(dir(pt))
print(pt._Point__x, pt._Point__y)
pt.check_value(5)
