class Server:
    count_server = 0

    def __new__(cls, *args, **kwargs):
        cls.count_server += 1
        return super().__new__(Server)

    def __init__(self):
        self.buffer = []
        self.ip = self.count_server
        self.router = None

    def send_data(self, data):
        self.buffer.append(data)

    def get_data(self):
        x = self.buffer
        self.buffer = []

        return x

    def get_ip(self):

        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.link_srv = []

    def link(self, server):
        self.link_srv.append(server)
        server.router = self

    def unlink(self, server):
        s = self.link_srv.remove(server)
        if s:
            s.router = None

    def clear_buffer(self):
        self.buffer = []

    def send_data(self):
        for i in self.buffer:
            for j in self.link_srv:
                if i.ip == j.ip:
                    j.buffer.append(i)
        self.clear_buffer()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
