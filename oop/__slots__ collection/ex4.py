class Note:
    _available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self._available_values:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    _available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __del__(self):
        Notes._instance = None

    def __init__(self):
        for k, v in zip(self.__slots__, self._available_values):
            setattr(self, k, Note(v, 0))

    def __getitem__(self, item):
        if not (0 <= item < 7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])


notes = Notes()
nota = notes[2]
print(nota)
notes[3].ton = -1
