import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name.lower()
        self.weight = weight
        self.price = price

    def __hash__(self):
        hash = (self.name, self.weight, self.price)
        return hash

    def __eq__(self, other):
        return (self.name == other.name and
                self.weight == other.weight and
                self.price == other.price)


lst = []
lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']
for i in lst_in:
    i.split()

for i in lst_in:
    x = ShopItem(i[0], i[1], i[2])
    lst.append(x)
shop_items = {}
print(*lst)

'''
Строки имеют следующий формат:
название товара 1: вес_1 цена_1
название товара N: вес_N цена_N
Например:
Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000
Как видите, товары в этом списке могут совпадать.
Необходимо для всех этих строчек сформировать соответствующие
объекты класса ShopItem и добавить в словарь с именем shop_items.
Ключами словаря должны выступать сами объекты, а значениями - список в формате:
[item, total]
где item - объект класса ShopItem; total - общее количество одинаковых объектов
(с одинаковыми хэшами). Подумайте, как эффективно программно наполнять такой словарь,
проходя по списку lst_in один раз.
P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.
'''
