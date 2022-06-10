a, k, b, m, x = map(int, input().split())

l = 0
r = 2 * x
while l + 1 < r:
	days = (l + r) // 2
	# посчитаем количество выходных дней у Дмитрия и Фёдора
	Dh = days // k
	Fh = days // m
	# сколько деревьев срубили Дмитрий и Фёдор за days дней
	trees = (days - Dh) * a + (days - Fh) * b
	if trees >= x:
		r = days
	else:
		l = days

print(r)
