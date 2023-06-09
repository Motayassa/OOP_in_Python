from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if type(number) != str:
            return False
        number_list = number.split('-')
        if len(number_list) != 4:
            return False
        if not all(map(lambda x: len(x) == 4, number_list)):
            return False
        return all(map(lambda x: x.isdigit(), number_list))

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        name_list = name.split(' ')
        if len(name_list) != 2:
            return False
        set_chars = set(cls.CHARS_FOR_NAME)
        return all(map(lambda x: set(x) < set(set_chars), name_list))
