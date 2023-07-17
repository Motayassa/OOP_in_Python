x, y = input().split()
try:
    res = int(x) + int(y)
except:
    try:
        res = float(x) + float(y)
    except:
        try:
            res = str(x) + str(y)
        except:
            pass
finally:
    print(res)
