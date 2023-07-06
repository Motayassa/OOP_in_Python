class IterColumn:
    def __init__(self, lst, column):
        self._lst = lst
        self._column = column

    def __iter__(self):
        for row in self._lst:
            yield row[self._column]


lst = [[11, 12, 'x1N'],
       [21, 22, 'x2N'],
       [1, 2, 'xMN']]
it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
