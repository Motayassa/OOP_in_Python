'''
__setattr__(self, key, value)__ – автоматически вызывается при
изменении свойства key класса;
__getattribute__(self, item) – автоматически вызывается при
получении свойства класса с именем item;
__getattr__(self, item) – автоматически вызывается при получении
несуществующего свойства item класса;
__delattr__(self, item) – автоматически вызывается при удалении
свойства item (не важно: существует оно или нет).
'''


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):  # автоматически вызывается,
        #  когда идет считывание атрибута через экземпляр класса.
        # Например, при обращении к свойству pt1.MIN_COORD
        if item == "_Point__x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # автоматически вызывается в момент
        # присваивания атрибуту нового значения
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)  # Смена свойства напрямую
            # если нужно self.__dict__[key] = value

    def __getattr__(self, item):  # автоматически вызывается,
        # если идет обращение к несуществующему атрибуту.
        # Например, нам необходимо определить класс, в котором при обращении
        # к несуществующим атрибутам возвращается значение False,
        # а не генерируется исключение.
        # print("__getattr__: " + item)
        return False

    def __delattr__(self, item):  # вызывается в момент удаления
        # какого-либо атрибута из экземпляра класса
        print("__delattr__: "+item)
        object.__delattr__(self, item)  # Непосредстыенные действия
        # выполняет класс object
        # Магические методы только перехватывают их, для изменения настроек

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.MIN_COORD)
# print(pt1._Point__x)
print(pt1.a)
print(pt1.MAX_COORD)
pt1.a = 10
del pt1.a
print(pt1.__dict__)
