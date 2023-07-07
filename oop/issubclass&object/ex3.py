class Protists:
    pass


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Create:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Monkey(Monkeys, Create):
    def __init__(self, name, weight, old):
        super().__init__(name, weight, old)


class Person(Human, Create):
    def __init__(self, name, weight, old):
        super().__init__(name, weight, old)


class Flower(Flowering, Create):
    def __init__(self, name, weight, old):
        super().__init__(name, weight, old)


class Worm(Worms, Create):
    def __init__(self, name, weight, old):
        super().__init__(name, weight, old)


lst_objs = [Monkey("мартышка", 30.4, 7),
            Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34),
            Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1),
            Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1),
            Worm("червь 2", 0.02, 1)]


lst_animals = [x for x in lst_objs if isinstance(x, Animals)]
lst_plants = [x for x in lst_objs if isinstance(x, Plants)]
lst_mammals = [x for x in lst_objs if isinstance(x, Mammals)]
