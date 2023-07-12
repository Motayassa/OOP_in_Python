class Track:
    def __init__(self, *points):
        if len(points) == 2 and type(points[0] in (int, float) and points[1] in (int, float)):
            self.__points = [PointTrack(points[0], points[1])]
        else:
            self.__points = list(points)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self.x = self.check_coords(x)
        self.y = self.check_coords(y)

    def check_coords(self, coord):
        if type(coord) not in (int, float):
            raise TypeError('координаты должны быть числами')

        return coord

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'


tr_0 = Track(0, 2)
tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
