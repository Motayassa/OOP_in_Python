class PhoneBook:
    def __init__(self):
        self.tel_list = []

    def add_phone(self, phone):
        self.tel_list.append(phone)

    def remove_phone(self, indx):
        self.tel_list.pop(indx)

    def get_phone_list(self):
        return self.tel_list


class PhoneNumber:
    def __init__(self, number, fio):
        self.__number = number
        self.__fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if all(lambda x: type(x) is int for x in number) and len(number) == 11:
            self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        if type(fio) is str:
            self.__number = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
