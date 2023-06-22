class HandlerGET:
    def __init__(self, func):  # Ссылка на декорируемую функцию
        self.func = func

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        # данный метод срабатывает при успешной проверке call
        return f'GET: {func(request)}'


request = {"method": "GET", "url": "contact.html"}


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
