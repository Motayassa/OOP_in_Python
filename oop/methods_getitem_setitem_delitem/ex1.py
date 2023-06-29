class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # создаем словарь в локальных атрибутах
        self.__total_attrs = len(kwargs)  # вспом. аттр - кол-во элементов слоавря
        self.__attrs = tuple(self.__dict__.keys())  # ключи словаря 

    def __check_indx(self, indx):
        if type(indx) != int or not (-self.__total_attrs <= indx <= self.__total_attrs):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__check_indx(item)
        return getattr(self, self.__attrs[item])

    def __setitem__(self, key, value):
        self.__check_indx(key)
        setattr(self, self.__attrs[key], value)


r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError