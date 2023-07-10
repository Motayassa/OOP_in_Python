class ItemAttrs:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attrs = list(self.__dict__.keys())

    def __getitem__(self, item):
        if type(item) != int:
            raise TypeError("Error")
        return self.attrs[item]

    def __setitem__(self, key, value):
        self.attrs[key] = value


class Point(ItemAttrs):
    pass


pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
