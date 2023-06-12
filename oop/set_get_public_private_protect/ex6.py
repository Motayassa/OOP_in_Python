'''Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.
'''
'''Для этого объявите класс LinkedList, который будет представлять связный список в целом и 
иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:

head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).'''


class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        pass

    def remove_obj(self):
        pass

    def get_data(self):
        pass


class ObjList:
    def __init__(self, next, prev, data):
        self.__next = next
        self.__prev = prev
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
