class Track:
    def __init__(self, start_x: int, start_y: int):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def add_track(self, tr):
        self.tracks.append(tr)

    def get_tracks(self):
        return tuple(self.tracks)

    def __len__(self):
        len_1 = ((self.start_x - self.tracks[0].x) ** 2 + (self.start_y - self.tracks[0].y)**2) ** 0.5
        return int(len_1 + sum(self.__get_length(1) for i in range(1, len(self.tracks))))

    def __get_length(self, i):
        return((self.tracks[i-1].x - self.tracks[i].x) ** 2 + (self.tracks[i-1].y - self.tracks[i].y) **2) ** 0.5

    def __eq__(self, other):
        if type(other) == Track:
            return len(self) == len(other)

    def __ne__(self, other):
        if type(other) == Track:
            return len(self) != len(other)

    def __lt__(self, other):
        if type(other) == Track:
            return len(self) < len(other)

    def __gt__(self, other):
        if type(other) == Track:
            return len(self) > len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    @property
    def x(self):
        return self.to_x

    @property
    def y(self):
        return self.to_y

    @property
    def max_speed(self):
        return self.max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = (track1 == track2)
'''
Создайте два маршрута track1 и track2 с координатами:
1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90
Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.'''