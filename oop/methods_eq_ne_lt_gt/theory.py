#  Магические методы для реализации операторов сравнения:
#
#          equal  __eq__()  –  для равенства ==
#      not equal  __ne__()  –  для неравенства !=
#      less than  __lt__()  –  для оператора меньше <
#     less equal  __le__()  –  для оператора меньше или равно <=
#   greater than  __gt__()  –  для оператора больше >
#  greater equal  __ge__()  –  для оператора больше или равно >=
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

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    '''def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc'''


c1 = Clock(1000)
c2 = Clock(2000)
# объекты сравниваются по их id (адресу в памяти), а мы бы хотели,
# чтобы сравнивались секунды в каждом из объектов c1 и c2
# Для этого переопределим магический метод __eq__()
print(c1 == c2)
print(c1 != c2)  # здесь применяется инверсия  not
print(c1 < c2)
print(c1 > c2)  # здесь меняется порядок операндов
print(c1 <= c2)
print(c1 >= c2)  # здесь меняется порядок операндов
