#  Оператор    Метод оператора
#
#   x + y    __add__(self, other)
#   x - y    __sub__(self, other)
#   x * y    __mul__(self, other)
#   x / y    __truediv__(self, other)
#   x // y   __floordiv__(self, other)
#   x % y    __mod__(self, other)
#
#   x += y   __iadd__(self, other)
#   x -= y   __isub__(self, other)
#   x *= y   __imul__(self, other)
#   x /= y   __itruediv__(self, other)
#   x //= y  __ifloordiv__(self, other)
#   x %= y   __imod__(self, other)

class Clock:
    __DAY = 86400   # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60            # секунды
        m = (self.seconds // 60) % 60    # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    '''def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Правый операнд должен быть типом int")

        return Clock(self.seconds + other)'''

    def __add__(self, other):  # сложение object + int
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):  # сложение int + object
        return self + other

    def __iadd__(self, other):  # oject += int
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc

        return self


# c1 = Clock(1000)
# print(c1.get_time())
# c1.seconds = c1.seconds + 100  # изменение времени в объекте с1
# c1 = c1 + 100  # Чтобы данная запись работала нужно добавить метод add
# с1 = c1.__add__(100)  # запись равно с1 = с1 + 100
'''c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())'''
c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c4 = c1 + c2 + c3
print(c4.get_time())
с5 = 100 + c1
с5 += 100
