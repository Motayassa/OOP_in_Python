class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

    @classmethod
    def __check_coords(cls, x, y):
        return type(x) is (int, float) and type(y) is (int, float)


class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):
        self.__sp = self.__ep = None

        if isinstance(x1, Point) and isinstance(y1, Point):
            self.set_coords(x1, y1)
        elif all(map(lambda x: type(x) in (int, float), (x1, y1, x2, y2))):
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()}{self.__ep.get_coords()}")


rect = Rectangle(0, 0, 20, 34)
rect.draw()
