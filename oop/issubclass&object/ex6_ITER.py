class IteratorAttrs:
    def __iter__(self):
        for x in self.__dict__.items():
            yield x


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('model', 'size', 1024)
for attr, value in phone:
    print(attr, value)
