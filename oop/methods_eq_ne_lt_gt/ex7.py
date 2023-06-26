'''Необходимо объявить класс Body (тело), объекты которого создаются командой:
body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное);
volume - объем тела  (число: вещественное или целочисленное).
Для объектов класса Body должны быть реализованы операторы сравнения:
body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:
m = ro * volume'''


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @staticmethod
    def mass(ro, volume):
        return ro * volume

    def __gt__(self, other):
        body1 = self.mass(self.ro, self.volume)
        body2 = self.mass(other.ro, other.volume)
        if type(other) == Body:
            return body1 > body2

    def __eq__(self, other):
        if type(other) == Body:
            body1 = self.mass(self.ro, self.volume)
            body2 = self.mass(other.ro, other.volume)
            return body1 == body2
        if type(other) in (int, float):
            body1 = self.mass(self.ro, self.volume)
            return body1 == 5

    def __lt__(self, other):
        body1 = self.mass(self.ro, self.volume)
        if type(other) in (int, float):
            return body1 < 10


b1 = Body('telo1', 2, 3)
b2 = Body('telo2', 0.5, 10)
b3 = Body('telo9', 0.5, 70)

