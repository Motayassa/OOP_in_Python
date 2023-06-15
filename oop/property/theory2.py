# Альтерантивный код из теории 1 с использованием декораторов
class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    '''
    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)
    old = old.deleter(del_old)
    '''
    @property
    def old(self):  # объект-свойство (ГЕТТЕР)
        return self.__old

    @old.setter  # СЕТТЕР
    def get_old(self, old):  # Метод set_old нужно переименовать в get_old,
        # чтобы имена совпадали (это обязательное условие)
        # и перед ним прописать декоратор
        self.__old = old

    @old.deleter  # ДЕЛИТЕР
    def old(self):
        del self.__old


p = Person('Сергей', 20)
print(p.get_old)
p.get_old = 35
print(p.get_old)
