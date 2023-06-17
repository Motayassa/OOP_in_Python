class Bag:
    def __init__(self, max_weight):
        self.total_weight = 0
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_weight - thing.weight >= 0:
            self.__things.append(thing)
            self.max_weight -= thing.weight
            self.total_weight += thing.weight

    def remove_thing(self, indx):
        x = len(self.things)
        if x == indx + 1 or x > indx + 1:
            self.max_weight += self.things[indx].weight
            self.total_weight -= self.things[indx].weight
            self.__things.pop(indx)

    def get_total_weight(self):
        return self.total_weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
