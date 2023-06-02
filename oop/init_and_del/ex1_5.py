class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y


points = [Point(i, i) for i in range(1, 2000, 2)]
