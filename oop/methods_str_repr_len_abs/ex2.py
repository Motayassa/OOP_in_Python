class Model:
    def __init__(self):
        self.count = None

    def query(self, **kwargs):
        self.count = kwargs

    def __str__(self):
        if self.count is None:
            return 'Model'
        else:
            return 'Model: ' + ', '.join([f'{key} = {value}'
                                          for key, value
                                          in self.count.items()])


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
