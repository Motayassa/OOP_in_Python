class Point:      
    '_Класс для представления координат точек на плоскости_'
    color = 'red' 
    circle = 2
    def __init__(self,x=0,y=0):    #икс и игрик определяются сразу после создания объекта экземпляра класса
        self.x = x
        self.y = y
    
    def __del__(self):     
        print ('удаление экземпляра'+ str(self))
    
pt = Point(1,2)
print(pt.__dict__)
