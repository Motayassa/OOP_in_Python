class Digit:
    def __init__(self, value):
        self.value = self.check_value(value)

    def check_value(self, value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        return value


class Integer(Digit):
    def check_value(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')
        return value


class Float(Digit):
    def check_value(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        return value


class Positive(Digit):
    def check_value(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        return value


class Negative(Digit):
    def check_value(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')
        return value


class PrimeNumber(Integer, Positive):
    def check_value(self, value):
        if type(value) != int or value <=0:
            raise TypeError('значение не соответствует типу объекта')
        for i in range(2, value):
            if value % i == 0:
                raise TypeError('значение не соответствует типу объекта')
        return value


class FloatPositive(Float, Positive):
    def check_value(self, value):
        if type(value) != float or value <= 0:
            raise TypeError('значение не соответствует типу объекта')


digits = [PrimeNumber(7), PrimeNumber(13), PrimeNumber(37),
          FloatPositive(1.12), FloatPositive(1.9), FloatPositive(10.12)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
