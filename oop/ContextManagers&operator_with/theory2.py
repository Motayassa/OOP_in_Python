'___________ПИШЕМ СВОЙ КЛАСС МЕНЕДЖЕРА КОНТЕКСТА___________'
# Давайте создадим свой класс менеджера, который бы контролировал
# работу при изменении списка: если программа в теле менеджера приводит к
# исключению (ошибке), то список должен оставаться прежним (без изменений):


class DefenerVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [1, 2]
with DefenerVector(v1) as dv:
    for i, a in enumerate(dv):
        dv[i] += v2[i]

print(v1)
