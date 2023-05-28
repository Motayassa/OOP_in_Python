import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields)!=len(lst_values):
            return False
        else:
            for i in range(len(fields)):
                setattr(self,str(fields[i]),lst_values[i])
            return True
        

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = ['12','RFHRFC','24']  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()