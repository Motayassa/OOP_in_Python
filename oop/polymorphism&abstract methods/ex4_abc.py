from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    count_id = 0

    def __new__(cls, *args, **kwargs):
        cls.count_id = cls.count_id + 1
        return super().__new__(cls)

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.count_id

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
form1 = ModelForm("Логин", "Пароль")
form2 = ModelForm("Логин", "Пароль")
form3 = ModelForm("Логин", "Пароль")
print(form3.get_pk())
