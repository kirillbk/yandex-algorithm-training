# B. Эффективный менеджмент

from heapq import heappush, heappop


n, w = map(int, input().split())
tasks = list()
for i in range(1, n + 1):
	a, t = map(int, input().split())
	tasks.append((a, a + t, i))

tasks.sort()
# добавим одного сотрудника
employees = [[],]
heap = [(-1, 0),]
for start, end, i in tasks:
	if start >= heap[0][0]:
		_, e = heappop(heap)
	else:
		e = len(employees)
		employees.append([])
	employees[e].append(i)
	heappush(heap, (end, e))

print(len(employees))
for e in employees:
	print(*e, end=' ')
print()
