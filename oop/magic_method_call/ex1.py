from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        n = randint(self.min_length, self.max_length)
        len_chars = len(self.psw_chars)
        return ''.join(self.psw_chars[randint(0, len_chars - 1)]
                       for _ in range(n))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd(), rnd(), rnd()]
print(*lst_pass)
