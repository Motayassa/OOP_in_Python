try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
else:  # необязательный блок else, который выполняется при штатном выполнении
    # кода внутри блока try, то есть, когда не произошло никаких ошибок
    print("Исключений не произошло")
finally:  # Вторым необязательным блоком является блок finally, который,
    # наоборот, выполняется всегда после блока try, вне зависимости
    # произошла ошибка или нет
    print("Блок finally выполняется всегда")


# finally для работы с файлами
# Здесь ошибка произойдет после открытия файла в строчке f.write(),
# поэтому файл остается открытым. Kюбой файл нужно закрывать даже при
# возникновении ошибок. Как раз здесь может пригодиться блок finally:
'''try:
    f = open("myfile.txt")
    f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
finally:
    if f:
        f.close()
        print("Файл закрыт")'''


# Следующая особенность работы блока finally связана с обработкой
# исключений внутри функций. Предположим, в функции вводятся два
# целых числа и возвращаются в виде кортежа:
def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as v:
        print(v)
        return 0, 0
    finally:
        print("finally выполняется до return")


x, y = get_values()
print(x, y)


'___________________Вложенные блоки try / except___________________'
try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except ZeroDivisionError:
        print("Деление на ноль")
except ValueError as z:
    print("Ошибка ValueError")


# Или, можно внутренний блок try вынести в функцию:
'''def div(a, b):
    try:
        return x / y
    except ZeroDivisionError:
        return "Деление на ноль"'''

# А, затем, вызвать в первом блоке try:
'''try:
    x, y = map(int, input().split())
    res = div(x, y)
except ValueError as z:
    print("Ошибка ValueError")'''


print(res)
