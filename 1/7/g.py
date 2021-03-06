# G. Детский праздник
# Организаторы детского праздника планируют надуть для него M воздушных шариков. С этой целью они пригласили N добровольных помощников, i-й среди которых надувает шарик за Ti минут, однако каждый раз после надувания Zi шариков устает и отдыхает Yi минут.
# Теперь организаторы праздника хотят узнать, через какое время будут надуты все шарики при наиболее оптимальной работе помощников, и сколько шариков надует каждый из них.
# (Если помощник надул шарик, и должен отдохнуть, но больше шариков ему надувать не придется, то считается, что он закончил работу сразу после окончания надувания последнего шарика, а не после отдыха).

# Формат ввода
# В первой строке входных данных задаются числа M и N (0 ≤ M ≤ 15000, 1 ≤ N ≤ 1000). Следующие N строк содержат по три целых числа - Ti, Zi и Yi соответственно (1 ≤ Ti, Yi ≤ 100, 1 ≤ Zi ≤ 1000).

# Формат вывода
# Выведите в первой строке число T - время, за которое будут надуты все шарики. Во второй строке выведите N чисел - количество шариков, надутых каждым из приглашенных помощников. Разделяйте числа пробелами. Если распределений шариков несколько, выведите любое из них.

m, n = map(int, input().split())
events = []
for i in range(n):
	t, z, y = map(int, input().split())
	time = t
	baloons = 0
	while baloons < m:
		for _ in range(z):
			events.append((time, i))
			time += t
			baloons += 1
		time += y

events.sort()
baloons = 0
ans = [0] * n
total_time = 0
for time, i in events:
	baloons += 1
	ans[i] += 1
	if baloons == m:
		total_time = time
		break

print(total_time)
print(*ans)
