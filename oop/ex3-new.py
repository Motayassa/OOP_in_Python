class Point:
    def __new__(cls,*args,**kwargs):        #cls ссылается на сам класс Point
        print('вызов __new__ для'+str(cls))
        return super().__new__(cls)          #__new__ запускает процесс создания объекта и должен возвращать адрес нового созданного объекта
                                    #super() ссылка на базовый класс object, в котором вызываем метод _new_
        
    def __init__(self, x=0,y=0):           #self ссылается на создаваемй экземляр класса
        print('вызов __init__ для'+ str(self))
        self.x=x
        self.y=y

pt=Point(1,2)
print(pt)