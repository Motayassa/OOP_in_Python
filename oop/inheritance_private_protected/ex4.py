class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = self.check_str(model)
        self._mass = self.check_value(mass)
        self._speed = self.check_value(speed)
        self._top = self.check_value(top)

    def check_str(self, value):
        if type(value) is not str:
            raise TypeError('неверный тип аргумента')
        return value

    def check_value(self, value):
        if type(value) not in (int, float):
            raise TypeError('неверный тип аргумента')
        if value <= 0:
            raise TypeError('неверный тип аргумента')
        return value


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self.check_chairs(chairs)

    def check_chairs(self, value):
        if type(value) != int:
            raise TypeError('неверный тип аргумента')
        if value <= 0:
            raise TypeError('неверный тип аргумента')
        return value


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = self.check_dict(weapons)

    def check_dict(self, obj):
        if type(obj) is not dict:
            raise TypeError('неверный тип аргумента')
        return obj


WarPlane('model2', 500, 3, 1000, {"ракета": 4, "бомба": 7})
planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
