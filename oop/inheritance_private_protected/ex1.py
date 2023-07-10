class Animal:
    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = []
x = ['Васька; дворовый кот; 5',
     'Рекс; немецкая овчарка; 8',
     'Кеша; попугай; 3']

for i in x:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    y = Animal(*args)
    animals.append(y)

print(animals)
