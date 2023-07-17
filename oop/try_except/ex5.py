class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float:
            raise ValueError('значение не прошло валидацию')
        if not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != int:
            raise ValueError('значение не прошло валидацию')
        if not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    res = []
    for value in lst:
        for validator in validators:
            try:
                validator(value)
                res.append(value)
                break
            except ValueError:
                pass
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)
