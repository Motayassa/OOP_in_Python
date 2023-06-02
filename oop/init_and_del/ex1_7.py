class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self, a, b, c):
        if (
            type(a) != 'int' or type(a) != 'float' or
            type(b) != 'int' or type(b) != 'float' or
            type(c) != 'int' or type(c) != 'float'
        ):
            return 1

        if (
            a < 0 or a == 0 or
            b < 0 or b == 0 or
            c < 0 or c == 0
        ):
            return 1

        if (
            a + b <= c or
            a + c <= b or
            b + c <= a
        ):
            return 2

        if (
            a + b > c and
            a + c > b and
            b + c > a
        ):
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle)
