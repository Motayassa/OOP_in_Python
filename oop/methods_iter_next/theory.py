# __iter__(self) – получение итератора для перебора объекта;
# __next__(self) – переход к следующему значению и его считывание.
list(range(5))
a = iter(range(5))
print(next(a))
print(next(a))


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        # устанавливаем начальное значение value и возвращаем
        # ссылку на объекта класса,
        # так как этот объект в нашем примере и есть итератор –
        # через него вызывается
        # магический метод __next__.
        return self


fr = FRange(0, 2, 0.5)
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
fr = FRange(0, 2, 0.5)
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))

it = iter(fr)
for x in fr:
    print(x)

fr = FRange(0, 2, 0.5)
it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
