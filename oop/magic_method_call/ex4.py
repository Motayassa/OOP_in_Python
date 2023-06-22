class DigitRetrieve:
    def __call__(self, numb, *args, **kwargs):
        if numb.isdigit():
            numb = int(numb)
            return numb
        if numb[0] == '-':
            if numb[1:].isdigit():
                numb = int(numb[1:]) * (-1)
                return numb
        return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]'''
print(digits)
