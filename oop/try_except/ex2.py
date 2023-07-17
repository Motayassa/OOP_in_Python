data_input = "1 -5.6 2 abc 0 False 22.5 hello world"
lst_in = data_input.split()


# вариант 1
sum1 = 0
for x in lst_in:
    try:
        x = int(x)
        sum1 += x
    except ValueError:
        continue
print(sum1)


# вариант 2
def check(x):
    try:
        return int(x)
    except ValueError:
        pass


sum2 = sum(list(map(int, filter(lambda x: check(x), lst_in))))
print(sum2)
