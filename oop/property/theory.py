class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    # old = 45
    # old = property(get_old, set_old)  альтернатива нижней  записи
    # объект property с
    # ссылкой на сеттер и геттер
    # ЭТУ СТРОЧКУ МОЖНО ПРОПИСАТЬ С ПОМОЩЬЮ ДЕКОРАТОРОВ(ниже)
    old = property()   # строка 13 - альтернатива
    old = old.setter(set_old)
    old = old.getter(get_old)


p = Person('Сергей', 20)
# p.set_old(35)
print(p.get_old())
print(p.old)
print(Person.old)  # объект property
p.old = 35
p.__dict__['old'] = 'old in object p'
print(p.old, p.__dict__)
a = property()
# a.getter()   декоратор для сеттера;
# a.setter()   декоратор для геттера;
# a.deleter()   декоратор для делитера.
