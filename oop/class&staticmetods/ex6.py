class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[msg] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(msg)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, number):
        for m in tuple(cls.msgs[-number:]):
            print(m)

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
