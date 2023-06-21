class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):  # Вызывается при
        # вызове класса
        self.__counter += step
        return self.__counter


c = Counter()
c2 = Counter()
'''c()  # благодаря добавлению магического метода __ CALL__ в наш класс,
# теперь можно вызывать его экземпляры подобно функциям через
# оператор круглые скобки.
# Классы, экземпляры которых можно вызывать подобно функциям,
# получили название ФУНКТОРЫ
c()
res = c()
res2 = c2()
print(res, res2)
'''
c(2)
c(10)
res = c()
res2 = c2(-5)
print(res, res2)
