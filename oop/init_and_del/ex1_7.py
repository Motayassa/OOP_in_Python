class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self, a, b, c):
        if (
            (type(self.a) not in (int, float)) or
            (type(self.b) not in (int, float)) or
            (type(self.c) not in (int, float))
        ):
            return 1

        if (
            self.a < 0 or self.a == 0 or
            self.b < 0 or self.b == 0 or
            self.c < 0 or self.c == 0
        ):
            return 1

        if (
            self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a
        ):
            return 2

        if (
            self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a
        ):
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle(a, b, c))
