# Нон Дата Дескрипторы имеют более низкий приоритет
# при возвращении атрибутов, чем Дата Дескрипторы
# В ДатаДескрипторах присвоение через p.y имеет
# больший приоритет, чем присовение через колллекцию dict


class RealValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

#    def __set__(self, instance, value):
#        setattr(instance, self.name, value)


class Point:
    x = RealValue()
    y = RealValue()

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1.5, 2.3)
pt.__dict__['x'] = 10.0
pt.y = 11
print(pt.x)
print(pt.y)
