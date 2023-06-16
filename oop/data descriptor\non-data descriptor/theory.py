''' NON-DATA DESCRIPTOR
class A:
    def __get__(self, instance, owner):
        return ...
'''
'''DATA DESCRIPTOR
class B:
    def __get__(self, instance, owner):
        return ...

    def __set__(self, instance, value):
        ...

    def __del__(self):
        ...
'''


class Point3D:
    def __init__(self, x, y, z):  # Формируются защищенные локальные
        # свойства (_одно подчеркивание)
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


p = Point3D(1, 2, 3)
print(p.__dict__)
