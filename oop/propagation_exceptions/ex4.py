class TupleLimit(tuple):
    def __new__(cls, lst, max_lenght):
        return super().__new__(cls)

    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        super().__init__()
        self.lst = lst

    def __str__(self):
        return ' '.join([str(x) for x in self.lst])

    def __repr__(self):
        return ' '.join([str(x) for x in self.lst])


digits = list(map(float, input().split()))
try:
    print(TupleLimit(digits, 5))
except ValueError as e:
    print(e)
