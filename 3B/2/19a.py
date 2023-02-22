# 19. Коммерческий калькулятор

from heapq import heapify, heappop, heappush


n = int(input())
a = list(map(int, input().split()))

heapify(a)
answer = 0
while len(a) > 1:
	sum = heappop(a) + heappop(a)
	heappush(a, sum)
	answer += sum * 0.05

print(f'{answer:.2f}')
