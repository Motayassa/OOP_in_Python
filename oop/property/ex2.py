class WindowDlg:
    def __init__(self, txt_title, value_width, value_height):
        self.__title = txt_title
        self.__width = None
        self.__height = None
        self.width = value_width
        self.height = value_height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value_width):
        if type(value_width) == int and 0 <= value_width <= 10000:
            if self.__width:
                self.show()
            self.__width = value_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value_height):
        if type(value_height) == int and 0 <= value_height <= 10000:
            if self.__height:
                self.show()
            self.__height = value_height


wnd = WindowDlg(120, 100, 50)
wnd.height = 1000