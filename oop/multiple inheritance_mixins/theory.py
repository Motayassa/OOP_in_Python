class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


# Этот класс работает совершенно независимо от классов Goods и
# Notebook и лишь добавляет функционал по логированию товаров
# с использованием их id. Такие независимые базовые классы и
# получили название миксинов – примесей.
class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")

    def print_info(self):
        print("print_info класса MixinLog")


class MixinLog2:
    def __init__(self):
        super().__init__()
        print("init MixinLog 2")


class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)  # цепочка обхода базовых классов
# MRO – Method Resolution Order
'''порядок следования базовых классов при множественном наследовании имеет
важное значение. Первым должен идти «основной» класс и у него, как правило,
инициализатор имеет несколько параметров. А далее, записываются классы, у
которых, опять же, как правило, инициализаторы имеют только параметр self.
Это второй важный момент. Когда мы собираемся использовать множественное
наследование, то структуру классов следует продумывать так, чтобы
инициализаторы вспомогательных классов имели только один параметр self,
иначе будут сложности их использования.'''
'''Чтобы в программах при множественном наследовании не возникало проблем с
зависимостью последовательности наследования дополнительных базовых классов,
их инициализаторы следует создавать с одним параметром self и в каждом из
них прописывать делегированный вызов инициализатора следующего класса командой:
super().__init__()'''
'__________Вызов методов с одинаковыми именами из базовых классов_____________'
n.print_info()
'''Понятно, что если сейчас его вызвать через объект класса NoteBook:
то мы обратимся к методу класса Goods, так как он записан первым в цепочке
наследования и в соответствии с алгоритмом обхода MRO он будет найден первым.
Но что если мы хотим вызвать этот метод из второго базового класса MixinLog?
Как поступить? Сделать это можно двумя способами. Либо напрямую вызвать этот
метод через класс MixinLog:'''
MixinLog.print_info(n)
'''Либо, определить какой-либо метод в классе NoteBook
(пусть он называется также)'''
'''class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)'''
'''Обычно, если нужно делать такие подмены, то есть, из конкретного дочернего
класса вызывать метод другого (не первого) базового класса, то создают метод
в дочернем классе с тем же именем, а затем,
явно указывают нужный базовый класс.'''