# F. Расстановка ноутбуков
# В школе решили на один прямоугольный стол поставить два прямоугольных ноутбука. Ноутбуки нужно поставить так, чтобы их стороны были параллельны сторонам стола. Определите, какие размеры должен иметь стол, чтобы оба ноутбука на него поместились, и площадь стола была минимальна.

# Формат ввода
# Вводится четыре натуральных числа, первые два задают размеры одного ноутбука, а следующие два — размеры второго. Числа не превышают 1000.

# Формат вывода
# Выведите два числа — размеры стола. Если возможно несколько ответов, выведите любой из них (но только один).

x1, y1, x2, y2 = map(int, input().split())
laptop1 = x1, y1
laptop2 = x2, y2

table = float('inf')
for i in range(2):
	for j in range(2):
		x = laptop1[i] + laptop2[j]
		y = max(laptop1[i - 1], laptop2[j - 1])
		if x * y < table:
			min_x = x
			min_y = y
			table = min_y * min_x

print(min_x, min_y)