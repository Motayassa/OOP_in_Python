def get_loss(w1, w2, w3, w4):
    try:
        w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        y = 10 * w1 // w2 - 5 * w2 * w3 + w4
        return y
