class ListInteger(list):
    def __init__(self, lst):
        for x in lst:
            self.__check_type(x)
        self.args = lst
        super().__init__(lst)

    @staticmethod
    def __check_type(x):
        if type(x) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.__check_type(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.__check_type(value)
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError'''
