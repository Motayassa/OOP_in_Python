data_input = "1 -5.6 True abc 0 23.56 hello"
lst_in = data_input.split()


def check_digit(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x


lst_out = [x for x in map(check_digit, lst_in)]
print(lst_out)
