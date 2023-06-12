from random import randint
from string import ascii_letters, digits


class EmailValidator:
    chars = ascii_letters + digits + '_@.'
    random_chars = ascii_letters + digits + '_'
    len_email = [range(11, 111)]

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.random_chars) - 1
        return ''.join(cls.random_chars[randint(0, length)] for i in range(n)) + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return None

        if not set(email) < set(cls.chars):
            return False

        s = email.split('@')
        if len(s) != 2:
            return False

        if len(s[0]) > 100 or len(s[1]) > 50:
            return False

        if '.' not in s[1]:
            return False

        if email.count('..') > 0:
            return False

        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str
