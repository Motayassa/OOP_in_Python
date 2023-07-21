class DateString:
    def __init__(self, date_string):
        self.date_string = self.check_format(date_string)
        self.day = self.date_string[0]
        self.month = self.date_string[1]
        self.year = self.date_string[2]

    def check_format(self, date):
        date = date.split('.')
        if len(date) != 3:
            raise DateError("Неверный формат даты")
        for i, j in enumerate(date):
            try:
                date[i] = int(j)
            except:
                raise DateError("Неверный формат даты")
        day, month, year = date
        if not 0 < day <= 31:
            raise DateError("Неверный формат даты")
        if not 0 < month <= 12:
            raise DateError("Неверный формат даты")
        if not 0 < year <= 9999:
            raise DateError("Неверный формат даты")
        return day, month, year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


class DateError(Exception):
    def __init__(self, *message):
        self.message = "Неверный формат даты"

    def __str__(self):
        return self.message


date_string = input()
try:
    date = DateString(date_string)
    print(date)  # date
except DateError as e:
    print(e)
except ValueError:
    print(DateError)
