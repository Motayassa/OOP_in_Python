def input_int_numbers(x):
    for i in x:
        try:
            i = int(i)
        except TypeError:
            raise TypeError('все числа должны быть целыми')
    else:
        return tuple(x)


flag = True
while flag:
    try:
        s = input().split()
        input_int_numbers(s)
        flag = False
    except:
        continue
else:
    print(*s)
