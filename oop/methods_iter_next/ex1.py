class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)  # все локадбные атрибуты
        self._len_attrs = len(self._attrs)  # кол во локальных атрибутов
        self._iter_index = -1  # индекс атрибута, который перебирают в итераторе

    def check_index(self, index):
        if type(index) != int or not (-self._len_attrs <= index < self._len_attrs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        return self.__dict__[self._attrs[item]]  # getattr(self, self._attrs[item])

    def __setitem__(self, key, value):
        self.check_index(key)
        setattr(self, self._attrs[key], value)

    def __next__(self):
        if self._iter_index < self._len_attrs - 1:
            self._iter_index += 1
            return getattr(self, self._attrs[self._iter_index])
        else:
            raise StopIteration

    def __iter__(self):
        self._iter_index = -1  # инициализация итератора
        return self  # сам объект класса бужет итератором

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
