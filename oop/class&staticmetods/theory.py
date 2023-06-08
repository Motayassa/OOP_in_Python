class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and self.validate(y):
            # Оба варианта обращения подъодят
            self.x = x
            self.y = y

        print(Vector.norm2(self.x, self.y))
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @classmethod  # Обращается только к атрибутам текущего класса,
    # но не к локальным свойствам его экзмепляров
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(10, 20)
coord = v.get_coord()
coord2 = Vector.get_coord(v)
print(coord)
print(coord2)
res = Vector.validate(5)
print(res)
res = Vector.norm2(5, 6)
print(res)
