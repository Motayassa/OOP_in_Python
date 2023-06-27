class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y



p = Point(0, 0)
p = Point(3, 4)
# эта функция всегда возвращает True для любых объектов
# пользовательского класса.
# Мы можем переопределить ее поведение либо через магический метод __len__(),
# либо через метод __bool__():
# __len__() – вызывается функцией bool(), если не определен магический метод __bool__();
# __bool__() – вызывается в приоритетном порядке функцией bool().
print(bool(p))
