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
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = args[0], args[1]
            self.__ep = args[2], args[3]

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.get_coords()}")


rect = Rectangle(0, 0, 20, 34)
