class Book:
    def __init__(self, author, title, price):
        if self.__check_str(author):
            self.__author = author
        if self.__check_str(title):
            self.__title = title
        if self.__check_pr(price):
            self.__price = price

    def set_title(self, title):
        if self.__check_str(title):
            self.__title = title

    def set_author(self, author):
        if self.__check_str(author):
            self.__author = author

    def set_price(self, price):
        if self.__check_pr(price):
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    @classmethod
    def __check_str(cls, strings):
        return type(strings) == str

    @classmethod
    def __check_pr(cls, price):
        return type(price) == int and price >= 0


book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
book.get_title()
book.get_author()
book.get_price()
