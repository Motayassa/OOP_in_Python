class ThreadData:      #ПАТТЕРН МОНОСОСТОЯНИЯ
    __shared_attrs = {    #приватный атрибут - словарь с общими локальными атрибутами класса
        'name': 'thread_1',
        'data':{},
        'id': 1
    }
    
    def __init__(self):  #инициализатор ссылает коллекцию dict на словарь, в итоге каждый созданный экземпляр класса имеет общие свойства
        self.__dict__ = self.__shared_attrs  #у каждого создаваемого объекта есть коллекция dict 
                                            #хранит локальные свойства экземпляра класса
                                        
# Паттерн моносостояния делает определенные атрибуты экземпляров класса общими, 
# изменение атрибута одного экземпляра меняет атрибут во всех экземплярах класса
# создание нового атрибута в экземпляре класса, создает в других экземплярах точно такой же
# т.е. локальное пространство имен стало единым для этих объектов

# меняя ссылку __DICT__ можно сильно менять поведение экземпляров класса касательно их локальных аттрибутов
