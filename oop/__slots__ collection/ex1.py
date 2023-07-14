class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


data_input = '''Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель'''.split('\n')
persons = []
for i in data_input:
    args = i.strip().split(',')
    persons.append(Person(args[0], args[1], args[2]))
