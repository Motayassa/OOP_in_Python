class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.lst = [self.__cell() for _ in range(self.__max_length)]

    def __getitem__(self, item):
        if type(item) != int or not (-self.__max_length <= item <= self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.lst[item].value

    def __setitem__(self, key, value):
        if type(key) != int or not (-self.__max_length <= key <= self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.lst[key].value = value

    def __repr__(self):
        return " ".join(map(str, self.lst))


class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError