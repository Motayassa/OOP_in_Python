class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_bs = []
lst_in = ['Python; Балакирев С.М.; 2020',
          'Python ООП; Балакирев С.М.; 2021',
          'Python ООП; Балакирев С.М.; 2022',
          'Python; Балакирев С.М.; 2021']
for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    x = BookStudy(*args)
    lst_bs.append(x)

unique_books = len(set(lst_bs))
