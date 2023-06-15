class Money:
    def __init__(self):
        self.__money = 0

    def set_money(self, value):
        self.__money = value

    def get_money(self):
        return self.__money

    money = property(get_money, set_money)


m = Money()
m.money = 10
m.__dict__['money'] = 100
res = m.money
print(res)
