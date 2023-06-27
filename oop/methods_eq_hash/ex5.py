'''Объявите класс с именем Dimensions, объекты которого создаются командой:
d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные),
описывающие габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные
атрибуты a, b, c (с соответствующими числовыми значениями). Также
для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.
С помощью функции input() прочитайте из входного потока строку, записанную в формате:
"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"
Например:
"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
Если какой-либо габарит оказывается отрицательным значением или равен нулю,
то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса
Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию)
хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.
'''