class Integer:  # Data Descriptor
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Point3D:
    x = Integer()  # Это дескрипторы данных, через которые будет проходить взаимодействие
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
print(pt.__dict__)
pt = Point3D('1', 2, 3)
