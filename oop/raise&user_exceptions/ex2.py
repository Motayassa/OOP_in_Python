class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if 'id' not in kwargs and 'pk' not in kwargs:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'
        else:
            key, value = tuple(kwargs.items())[0]
            self.message = f'Значение первичного ключа {key} = {value} недопустимо'

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
