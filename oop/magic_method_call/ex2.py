class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, string, *args, **kwargs):
        start = string.rfind('.')
        ext = '' if start == -1 else string[start + 1:]
        return ext in self.extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg",
             "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))
