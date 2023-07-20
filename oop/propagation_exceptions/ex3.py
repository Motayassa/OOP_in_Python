from abc import abstractmethod


class Test:
    def __init__(self, descr):
        self._descr = self.__check_len(descr)

    def __check_len(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        return descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = self.__check_digit(ans_digit)
        self.__check_value(max_error_digit)
        self.max_error_digit = self.__check_digit(max_error_digit)

    @staticmethod
    def __check_digit(value):
        if type(value) not in (int, float):
            raise ValueError('недопустимые значения аргументов теста')
        return value

    @staticmethod
    def __check_value(value):
        if not value >= 0:
            raise ValueError('недопустимые значения аргументов теста')

    def run(self):
        ans = float(input())
        if not self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit:
            return False
        return True


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение
# получится при вычислении 2+2? | 4
ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок
# в преобразовании быть не может
try:
    test = TestAnsDigit(descr, ans)
    res = test.run()
    print(res)
except ValueError as e:
    print(e)
except NotImplementedError as z:
    print(z)
