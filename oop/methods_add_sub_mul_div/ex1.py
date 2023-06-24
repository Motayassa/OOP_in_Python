class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    @staticmethod
    def __list_subtraction(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [x for x in lst1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError('Правый оператор должен иметь тип лист или ньюлист')
        other_list = other if type(other) == list else other.get_list()
        return self.__class__(self.__list_subtraction(self._lst, other_list))

    def __rsub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError('Правый оператор должен иметь тип лист')
        return self.__class__(self.__list_subtraction(other, self._lst))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1._lst)
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
