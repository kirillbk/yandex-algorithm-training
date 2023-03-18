# 11. Конвейер

def solution(a: list[float]) -> int:
	store = list()
	b = 0

	for item in a:
		if store and item > store[-1]:
			while store and store[-1] <= item and store[-1] >= b:
				b = store.pop()
		store.append(item)

	while store and store[-1] >= b:
		b = store.pop()

	if store:
		return 0
	return 1


n = int(input())
for _ in range(n):
	a = list(map(float, input().split()[1:]))
	print(solution(a))

