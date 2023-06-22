class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ('ul','ol') else 'ul'

    def __call__(self, list, *args, **kwargs):
        start_tag = f'<{self.type_list}>'
        finish_tag = f'</{self.type_list}>'
        lines = [start_tag]
        for _ in lst:
            line = '<li>' + _ + '</li>'
            lines.append(line)
        lines.append(finish_tag)
        return '\n'.join(lines)

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("pppol")
html = render(lst)
print(html)
