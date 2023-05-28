import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000','3 Иван 13 1200']  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):  
        '''select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] 
        (включительно) по их индексам (не id, а индексам списка); также учесть, что граница b может
        превышать длину списка.'''
        return self.lst_data[a:b+1]
        
        
    def insert(self, data):
        '''insert(self, data) - для добавления в список lst_data новых данных 
        из переданного списка строк data'''
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split(' '))))

    
db = DataBase()
db.insert(lst_in)
