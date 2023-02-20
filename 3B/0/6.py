# 6. Операционные системы lite

m = int(input())
n = int(input())
partitions = list()
systems = set()
for i in range(n):
	a, b = map(int, input().split())
	systems.add(i)
	for p_a, p_b, p_i in partitions:
		if a <= p_b and b >= p_a:
			systems.discard(p_i)
	partitions.append((a, b, i))
print(len(systems))
