# 14. Сортировка вагонов lite

n = int(input())
a = map(int, input().split())

number = 1
deadend = list()
for item in a:
	deadend.append(item)
	while deadend and deadend[-1] == number:
		deadend.pop()
		number += 1

if deadend:
	print('NO')
else:
	print('YES')
