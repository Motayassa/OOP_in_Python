class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        res = []
        for i, j in self.__dict__.items():
            res.append(f'{i}: {j}')
        return '\n'.join(res)


class ShopUserView:
    def __repr__(self):
        res = []
        for i, j in self.__dict__.items():
            if i == '_id':
                continue
            res.append(f'{i}: {j}')
        return '\n'.join(res)


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _title: Python ООП
# _author: Балакирев
# _year: 2022