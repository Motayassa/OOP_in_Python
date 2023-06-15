class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @classmethod
    def __is_verify(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__is_verify(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__is_verify(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


R = RadiusVector2D()
R = RadiusVector2D(1, 4)
R = RadiusVector2D(1)
