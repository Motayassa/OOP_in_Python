'_____________________ПОЛИМОРФИЗМ________________________'
# Возможность работы с разными объектами единым образом
# Во всех классах нужно переименовать метод единым образом


class Geom:  # ___________АБСТРАКТНЫЙ МЕТОД______________
    # Абстрактный метод не имеет собственной реализации и обязательно должен
    # быть переопределен программой
    '''def get_pr(self):  # вынесение за скобки метода get_pt
        return -1         # способ контроля без генерации исключения'''

    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w+self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
        # return self.a + self.b + self.c


geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]  # читабельная форма заполнения списка как сторона полиморфизма

for g in geom:  # единая конструкция для работы
    # с разными объектами
    print(g.get_pr())
