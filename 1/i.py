# I. Узник замка Иф
# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E. Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.

# Формат ввода
# Программа получает на вход числа A, B, C, D, E.

# Формат вывода
# Программа должна вывести слово YES или NO.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# отсортируем по возрастанию d и e
if d > e:
	d, e = e, d
# отсортируем по возрастанию a, b и c
if a > b:
	a, b = b, a
if b > c:
	b, c = c, b
if a > b:
	a, b = b, a

if a <= d and b <= c:
	print("YES")
else:
	print("NO")
