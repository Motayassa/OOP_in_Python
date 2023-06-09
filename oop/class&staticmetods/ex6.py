class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[msg] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(msg)

    def set_like(self):
        if self.fl_like:
            self.fl_like = False
        else:
            self.fl_like = True

    @classmethod
    def show_last_message(cls, n):
        list = [cls.msgs.keys()]
        print(list[:len(list) - n - 1:-1])

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
