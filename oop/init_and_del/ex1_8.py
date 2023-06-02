'''Прочитайте из входного потока числовые данные с помощью команды:
data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(),
затем метод set_show() со значением fl_show = False и вызовите метод show_table().
На экране должны отобразиться две соответствующие строки.'''


class Graph:
    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print("Отображение данных закрыто")
            print(*self.data, sep=' ')
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print("Графическое отображение данных: ", end='')
            print(*self.data, sep=' ')
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print("Столбчатая диаграмма: ", end='')
            print(*self.data, sep=' ')
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show
