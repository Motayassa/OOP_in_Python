class FileAcceptor:
    def __call__(self, *args):
        for arg in args:
            if arg.split(".")[-1] not in self.filenames:
                return False
            else:
                return True

    def __init__(self, *args):
        self.filenames = list(args)

    def __add__(self, other):
        if type(other) == FileAcceptor:
            new_flnm = self.filenames
            for i in other.filenames:
                if i not in new_flnm:
                    new_flnm.append(i)
            return self.__class__(*new_flnm)


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
