class PolyLine:
    def __init__(self, *args):
        self.coords = []
        for _ in args:
            self.coords.append(_)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return list(self.coords)


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(poly.get_coords())
