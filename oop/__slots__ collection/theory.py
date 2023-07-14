import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

pt = Point(1, 2)
print(pt.__dict__)
pt.x
pt.y = 100
pt.z = 4
print(pt.__dict__)


class Point2D:
    __slots__ = ('x', 'y')  # slots
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt2 = Point2D(10, 20)
pt2.x
pt2.y
print(pt2.__slots__)
# print(pt2.__dict__) эта коллекция пропадает при использовании SLOTS
pt2.x = 50
del pt2.y
pt2.y = 100
# мы совершенно спокойно можем изменять, удалять и
# добавлять локальные свойства x, y:
# Но только их и никакие другие. Причем, обратите внимание, речь идет
# только о локальных свойствах экземпляров. В сам класс мы по-прежнему
# можем добавлять любые атрибуты, например, MAX_COORD
print(pt.__sizeof__(), pt.__dict__.__sizeof__())
print(pt2.__sizeof__())
# Коллекция __slots__ помимо ограничения создаваемых локальных свойств,
# еще уменьшает объем памяти, занимаемый экземпляром класса.
t1 = timeit.timeit(pt.calc)
t2 = timeit.timeit(pt2.calc)

print(t1, t2)
# коллекция__slots__ускоряет работу с локальными свойствами экземпляров класса
# Вот такие три особенности дает коллекция __slots__ экземплярам класса:
# ограничение создаваемых локальных свойств;
# уменьшение занимаемой памяти;
# ускорение работы с локальными свойствами.
