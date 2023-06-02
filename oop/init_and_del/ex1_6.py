import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


LIST_CLASSES = [Line, Rect, Ellipse]
randcl = random.choice(LIST_CLASSES)
elements = [Line(0, 0, 0, 0)
            if randcl == Line
            else randcl(a=random.randrange(-100, 100),
                        b=random.randrange(-100, 100),
                        c=random.randrange(-100, 100),
                        d=random.randrange(-100, 100))
            for i in range(217)]
