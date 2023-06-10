'''Server - для описания работы серверов в сети;
Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
Data - для описания пакета информации.'''

'''send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
(пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
get_ip() - возвращает свой IP-адрес.

Соответственно в объектах класса Server должны быть локальные свойства:

buffer - список принятых пакетов (объекты класса Data, изначально пустой);
ip - IP-адрес текущего сервера.'''

class Server:
    count_server = 0

    def __new__(cls, *args, **kwargs):
        cls.count_server += 1
        return super().__new__(Server)

    def __init__(self):
        self.buffer = []
        self.ip = Server.count_server

    def send_data(data):
        pass

    def get_data(self):
        x = self.buffer
        self.buffer = []

        return x

    def get_ip(self):

        return self.ip


class Router:
    pass


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
