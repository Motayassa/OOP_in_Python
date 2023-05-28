from accessify import private, protected   #импортирование стороннего модуля

class Point:
    def __init__(self,x=0,y=0):
        self.__x=0
        self.__y=0
        if self.check_value(x) and self.check_value(y):
            self.__x=x
            self.__y=y
    
    @private   #декоратор из стороннего модуля
    @classmethod
    def check_value(cls,x): 
        return type(x) in (int,float)
        
    def set_coord(self,x,y):  #setter
        if self.check_value(x) and self.check_value(y):
            self.__x=x
            self.__y=y
        else:
            raise ValueError("Координаты должны быть числами")
    
    def get_coord(self):       #getter
        return self.__x, self.__y
    
pt = Point(1,2)
pt.set_coord(10,20)
print(pt.get_coord())
#print(pt._Point__x)  #шаблон обращения к приватному свойству извне
pt.check_value(5)

#РЕЖИМЫ ДОСТУПА 
#Механизмы инкапсуляции
# attribute --> public  
# _attribute --> protected  - внутри класса и дочерних классах - сигнал кодеру, явно не мешает доступу извне - НЕ ИСПОЛЬЗУЙ ВНЕ КЛАССА!!
                            # внутрення служебная переменная
# __attribute --> private  - только внутри класса

#ИНТЕРФЕЙСНЫЕ МЕТОДЫ - доп методы для работы с приватными атрибутами
    #сеттеры и геттеры  - взаимодействовать с атрибутами класса лучше через публичные атрибуты - поэтому создают вспомогательные методы
