class Float:
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError(
                "Присваивать можно только вещественный тип данных."
                )

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = Float()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)]for _ in range(n)]


table = TableSheet(5, 3)
N = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = N
        N += 1.0
