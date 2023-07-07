class Tuple(tuple):
    def __init__(self, iter_obj):
        self.__check_obj(iter_obj)
        if type(iter_obj) != tuple:
            self.iter_obj = tuple(iter_obj)
        else:
            self.iter_obj = tuple(iter_obj)

    def __add__(self, other):
        self.__check_obj(other)
        other = tuple(other)
        return self.__class__(self.iter_obj + other)

    @staticmethod
    def __check_obj(obj):
        if type(obj) not in (list, dict, str, set, tuple):
            return TypeError('Объект не итерируемый')


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)