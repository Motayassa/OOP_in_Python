class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i, 'yellow')
          if i == 3
          else Point(i, i)
          for i in range(1, 2000, 2)]
