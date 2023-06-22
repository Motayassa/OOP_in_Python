class Handler:
    def __init__(self, methods=("GET", )):
        self.__methods = methods
# т.к. в инициаторе есть параметры(methods), то декоратором мы
# делаем метод CALL (c помощью wrapper)

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            m = request.get('method', 'GET')
            if m in self.__methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)  # здесь
            # формируется сслыка на тот или иной метод

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)
