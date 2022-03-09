# H. Охрана
# На секретной военной базе работает N охранников. Сутки поделены на 10000 равных промежутков времени, и известно когда каждый из охранников приходит на дежурство и уходит с него.
# Например, если охранник приходит в 5, а уходит в 8, то значит, что он был в 6, 7 и 8-ой промежуток (а в 5-й нет!!!).
# Укажите, верно ли что для данного набора охранников, объект охраняется в любой момент времени хотя бы одним охранником и удаление любого из них приводит к появлению промежутка времени, когда объект не охраняется.

# Формат ввода
# В первой строке входного файла записано натуральное число K (1 ≤ K ≤ 100) — количество тестов в файле.
# Каждый тест начинается с числа N (1 ≤ N ≤ 10000), за которым следует N пар неотрицательных целых чисел A и B — время прихода на дежурство и ухода (0 ≤ A ≤ B ≤ 10000) соответствующего охранника.

# Формат вывода
# Выведите K строк, где в M-ой строке находится слово Accepted, если M-ый набор охранников удовлетворяет описанным выше условиям. В противном случае выведите Wrong Answer.

# Решение из разбора

def check_security(line):
	IN = -1
	OUT = 1
	data = map(int, line)
	n = next(data)
	events = []
	for i in range(n):
		events.append((next(data), IN, i))
		events.append((next(data), OUT, i))
	events.sort()

	necessary_security = set()
	cur_security = set()
	prev_event_time = -1
	for time, event, i in events:
		if time != 0 and not cur_security:
			return 'Wrong Answer'
		if len(cur_security) == 1 and prev_event_time != time:
			necessary_security.update(cur_security)
		if event == IN:
			cur_security.add(i)
		else:
			cur_security.remove(i)
		prev_event_time = time
	if events[-1][0] != 10000:
		return 'Wrong Answer'
	return 'Accepted' if len(necessary_security) == n else 'Wrong Answer'

k = int(input())
ans = [None] * k
for i in range(k):
	ans[i] = check_security(input().split())
print('\n'.join(ans))
