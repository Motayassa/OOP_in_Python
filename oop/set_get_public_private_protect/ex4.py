class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        if self.__check_coord(x1, y1, x2, y2):
            self.__x1 = x1
            self.__y1 = y1
            self.__x2 = x2
            self.__y2 = y2

    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2, sep=' ')

    @classmethod
    def __check_coord(cls, x1, y1, x2, y2):
        return all([lambda x: type(x) == int for i in (x1, y1, x2, y2)])
