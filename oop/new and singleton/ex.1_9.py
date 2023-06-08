class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def clone(self):
        pass


pt = Point(12, 7)
