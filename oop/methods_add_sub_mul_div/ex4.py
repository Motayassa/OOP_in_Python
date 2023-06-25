class Lib:
    def __init__(self):
        self.book_list = []

    @staticmethod
    def verify_type(book):
        return type(book) == Book

    def __add__(self, other):
        if self.verify_type(other):
            self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
            return self
        if type(other) == int:
            self.book_list.pop(other)
            return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
