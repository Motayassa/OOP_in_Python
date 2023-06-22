from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if type(real) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if type(img) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = img

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
