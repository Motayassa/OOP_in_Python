class Translator:
    '''для перевода с английского на русский'''
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        '''- для удаления связки по указанному английскому слову'''
        del self.tr[eng]

    def translate(self, eng):
        '''- для перевода с английского на русский
        (метод должен возвращать список из русских слов,
        соответствующих переводу английского слова,
        даже если в списке всего одно слово)'''
        return self.tr[eng]


tr = Translator()
line_in = '''tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко'''
line_in = list(line_in.split('\n'))
for i in line_in:
    eng_word, rus_word = i.split(' - ')
    tr.add(eng_word, rus_word)
tr.remove('car')
print(*tr.translate('go'))
