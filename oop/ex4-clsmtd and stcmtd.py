class Vector:      # прописывать имя класса в самом классе не стоит, нужно использовать self and cls  и тд
    MIN_COORD = 0
    MAX_COORD = 100
                        #@classmethod - декоратор метода класса
    @classmethod        #метод класса может обращаться только к атрибутам класса Vector
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <=cls.MAX_COORD
    
    def __init__(self,x,y):
        self.x = 0
        self.y = 0
        if self.validate(x) and self.validate(y):
            self.x=x
            self.y=y
            
        print(self.norm2(self.x,self.y))   #вызов статического метода внутри класса
        
    def get_coord(self):
        return self.x, self.y
    
    @staticmethod       #декорататор статического метода, не иммет доп параметров 
    def norm2(x,y):     #не обращается ни к классу, ни к его экземплярам - независмая функция внутри класса
       return x*x+y*y    # к атрибутам класса обращаться можно (Max/Min COORD), но только через имя класса Vector
    
v= Vector(1,20)
print(Vector.norm2(5,6))
#print(Vector.validate(5)) # метод класса можно вызывать через сам класс и без указания объекта cls в аргументе
                           # интерпретатор делает это автоматически, в этом отличие от обычного вызова класса
res = Vector.get_coord(v)  #вызов обычного класса, с указанием конкретного экземпляра класса
print(res)