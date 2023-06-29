class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def __len__(self):
        return len(self.tracks)

    def __check_indx(self, indx):
        if type(indx) != int or not (0 <= indx <= len(self) - 1):
            raise IndexError('некорректный индекс')

    def add_point(self, x, y, speed):
        self.tracks.append([x, y, speed])

    def __getitem__(self, item):
        self.__check_indx(item)
        return (self.tracks[item][0], self.tracks[item][1]), self.tracks[item][2]

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self.tracks[key][-1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2
tr[2] = 60
c, s = tr[2]
print(c, s)
res = tr[3]  # IndexError
