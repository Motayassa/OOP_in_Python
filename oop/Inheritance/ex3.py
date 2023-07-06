class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods)

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        f = getattr(self, method.lower(), False)
        if f:
            return f(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request.keys():
            raise TypeError('request не содержит обязательного ключа url')

        return f"url: {request['url']}"

#  СВОЙСТВА
#  getattr(obj,name[,default]) - возвращает значение атрибута объекта
#  hasattr(obj,name) - проверяет на наличие атрибута name в  obj
#  setattr(obj,name,value) - задает значение атрибута
# (если атрибут не существует,то он создается)
#  delattr(obj,name) - удаляет атрибут с именем name


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)
