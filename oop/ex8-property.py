class Person:
    def __init__(self,name,old):
        self.__name = name
        self.__old = old
    
    @property  #теперь геттер предствляет собой объект свойства для считывания приватного свойства __old
    def old(self):
        return self.__old
                    # setter так как есть такой декратор в property
    @old.setter  # имя такое потому что get old стал объектом property
    def old(self,old):
        self.__old = old
                                    #приватное локальное свойство property _Person__old
    #    old = property(get_old, set_old)  #old-объект класса property
   # old=property()  #property имеет три функции три декоратора - setter, getter, deleter
   # old=old.setter(set_old)
   # old=old.getter(get_old)
   
    @old.deleter
    def old(self):
        del self.__old

        
p = Person('сергей', 20)
del p.old
#p.__dict__['old'] = 'old in object p'  #явно добавляем локальный атрибут - приоритет будет ниже чем у свойства propperty
#a=p.old  #getter (при считывании данныых обЪект property автоматически вызывает геттер из объекта old)
p.old=35 #setter (при записи данных автоматически вызывается сеттер из оббъекта  old)
print(p.__dict__)

#Property позволяет взаимодествовать с приватным свойством old через одн атрибут old, обращаясь к сеттерам и геттерам
#если в классе задан атрибут-свойство(property)
#то в первую очередь выбирается оно, даже если в экземпляре класса есть локальный атрибут с таким же именем
#приоритет propperty выше чем у любого локального свойства (old приняло значение  35, хоть ранее было указано другое значение)