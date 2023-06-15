class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    # old = 45
    old = property(get_old, set_old)  # альтернатива нижней  записи
    # объект property с
    # ссылкой на сеттер и геттер
    # ЭТУ СТРОЧКУ МОЖНО ПРОПИСАТЬ С ПОМОЩЬЮ ДЕКОРАТОРОВ(ниже)
    '''
    old = property()   # строка 13 - альтернатива
    old = old.setter(set_old)
    old = old.getter(get_old)
    '''


p = Person('Сергей', 20)
# p.set_old(35)
print(p.get_old())
print(p.old)
del p.old
print(p.__dict__)
p.old = 10