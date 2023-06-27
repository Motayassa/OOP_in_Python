class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self, letter):
        self.inbox_list.append(letter)


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def __bool__(self):
        return self.is_read

    def set_read(self, fl_read=True):
        self.is_read = fl_read


lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
       'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
       'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
lst = []
mail = MailBox()

for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    item = MailItem(*args)
    lst.append(item)

for j in lst:
    mail.receive(j)

mail.inbox_list[0].set_read()
mail.inbox_list[-1].set_read()

inbox_list_filtered = list(filter(bool, mail.inbox_list))
