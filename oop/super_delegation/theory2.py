class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")

#l = Line(0, 0, 10, 20)  # Сначала вызывается __call__(), который, в свою очередь,
# последовательно вызывает метод __new__() для создания экземпляра класса,
# а затем, метод __init__() для его инициализации. Так вот, все эти методы
# вызываются из дочернего класса Line. Если какой-либо из них не находится,
# то поиск продолжается в родительских классах в порядке иерархии наследования.
# Например, метод __new__() в данном случае будет взят из метакласса type,
# который неявно вызывается при создании классов.
# А вот метод __init__() мы прописали в классе Geom,
# поэтому будет вызван именно он. Причем, параметр self в этом методе будет
# ссылаться на созданный объект класса Line. 
l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)