class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):  # singleton -
        # создание нового объекта класса
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


class Game2(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


s = Singleton()
s1 = Game('10')
s2 = Game('20')
s3 = Game2('30')
print(s1.name, s2.name, s3.name)
