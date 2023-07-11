class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __call__(self, data):
        return self._is_valid(data)

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) != float:
            return False
        if not self.min_value <= data <= self.max_value:
            return False

        return True


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
