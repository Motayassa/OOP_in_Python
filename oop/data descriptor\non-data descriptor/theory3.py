# Замена обращений к коллекции dict на специальные методы взаимодействия с аттрибутами


class Integer:  # Data Descriptor
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class ReadIntX:  # NonData Descriptor
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Point3D:
    x = Integer()  # Это дескрипторы данных, через которые будет проходить взаимодействие
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    xr = ReadIntX()


pt = Point3D(1, 2, 3)
print(pt.__dict__)
print(pt.xr)
pt.xr = 5
print(pt.xr, pt.__dict__)