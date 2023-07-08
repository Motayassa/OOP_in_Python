from string import digits


class StringDigit(str):
    def __init__(self, string):
        self.check_str(string)
        self.string = string

    @staticmethod
    def check_str(str):
        for i in str:
            if i not in digits:
                raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self.check_str(other)
        return self.__class__(self.string + other)

    def __radd__(self, other):
        self.check_str(other)
        return self.__class__(other + self.string)


sd = StringDigit("123")
print(sd)        # 123
sd = sd + "456"  # StringDigit: 123456
print(sd)
sd = "789" + sd  # StringDigit: 789123456
print(sd)
sd = sd + "12f"  # ValueError
