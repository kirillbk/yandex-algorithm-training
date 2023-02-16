# 6. Операционные системы lite

m = int(input())
n = int(input())
partitions = list()
systems = set()
for i in range(n):
	a, b = map(int, input().split())
	systems.add(i)
	for p_a, p_b, n in partitions:
		if a <= p_a <= b or a <= p_b <= b or p_a <= a <= p_b or p_a <= b <= p_b:
			systems.discard(n)
	partitions.append((a, b, i))
print(len(systems))
