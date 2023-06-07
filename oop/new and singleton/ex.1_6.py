class AbstractClass:
    x = "Ошибка: нельзя создавать объекты абстрактного класса"

    def __new__(cls, *args, **kwargs):
        # super().__new__(cls)
        return cls.x


obj = AbstractClass()
print(obj)
