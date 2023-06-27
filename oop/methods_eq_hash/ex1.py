class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        x = (self.width, self.height)
        return hash(x)


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)
h1, h2 = hash(r1), hash(r2)
print(h1 == h2)
