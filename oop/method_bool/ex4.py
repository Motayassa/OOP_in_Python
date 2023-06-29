class Ellipse:
    def __init__(self, *args, **kwargs):
        self.lenarg = len(args)
        if self:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return self.lenarg == 4

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(1, 1, 2, 2)]
for i in lst_geom:
    if i:
        i.get_coords()
'''
Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих
координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).
'''