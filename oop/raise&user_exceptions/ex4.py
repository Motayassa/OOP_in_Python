class CellException(Exception): pass


class Cell:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, '_' + k, v)
        self._v = None

    @property
    def value(self):
        return self._v

    @value.setter
    def value(self, v):
        self._v = self._is_valid(v)

    def _is_valid(self, v):
        raise NotImplemented('Метод должен быть переопреден в дочернем классе')


class CellIntegerException(CellException): pass


class CellFloatException(CellException): pass


class CellStringException(CellException): pass


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, v):
        if not self._min_value <= v <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        return v


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, v):
        if not self._min_value <= v <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')  
        return v


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _is_valid(self, v):
        if not self._min_length <= len(v) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        return v


class TupleData:
    def __init__(self, *args):
        [self.__is_cell(x) for x in args]
        self.cells = tuple(args)

    @staticmethod
    def __is_cell(x):
        if not isinstance(x, Cell):
            raise TypeError('______________')

    def __getitem__(self, item):
        return self.cells[item].value

    def __setitem__(self, key, value):
        self.cells[key].value = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for x in self.cells:
            yield x.value
