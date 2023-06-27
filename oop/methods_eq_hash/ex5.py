class Dimensions:
    def __init__(self, a, b, c):
        if '.' in a:
            self.a = float(a)
            self.check(self.a)
        else:
            self.a = int(a)
            self.check(self.a)
        if '.' in b:
            self.b = float(b)
            self.check(self.b)
        else:
            self.b = int(b)
            self.check(self.b)
        if '.' in c:
            self.c = float(c)
            self.check(self.c)
        else:
            self.c = int(c)
            self.check(self.c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def check(self, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return True


lst_dims = []
x = "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
lst = [x.split() for x in list(map(str.strip, x.split(';')))]
print(lst)
for i in lst:
    a, b, c = i[0], i[1], i[2]
    x = Dimensions(a, b, c)
    lst_dims.append(x)
lst_dims.sorted(key=hash)
print(lst_dims)