class MoneyR:
    EPS = 0.1
    type_money = 'rub'

    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, v):
        self.__volume = v

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        self.__cb = obj

    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return v1 < v2

    def __le__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return v1 <= v2


class MoneyD:
    EPS = 0.1
    type_money = 'dollar'

    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, v):
        self.__volume = v

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        self.__cb = obj

    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return v1 < v2

    def __le__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return v1 <= v2


class MoneyE:
    EPS = 0.1
    type_money = 'euro'

    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, v):
        self.__volume = v

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        self.__cb = obj

    def __eq__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return v1 < v2

    def __le__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = self.volume / other.cb.rates[other.type_money]
        return v1 <= v2


class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money):
        money.cb = cls

    def convertation(self, money):
        if type(money) == MoneyR:
            return money
        if type(money) == MoneyD:
            return money * self.rates['dollar']
        if type(money) == MoneyE:
            return money * self.rates['euro']

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
