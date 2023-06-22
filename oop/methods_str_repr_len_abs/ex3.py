class WordString:
    def __init__(self, *args):
        self.string = args[0]

    def __call__(self, indx, *args, **kwargs):
        self.indx = indx
        lst = self.string.split()
        if indx <= len(self.string):
            return lst[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, st):
        if '  ' in st:
            while '  ' not in st:
                st.replace('  ', ' ')
        self.__string = st

    def __len__(self):
        return len(self.string.split())


words = WordString("Курс по Python ООП")
print(len(words))
print(words(2))
