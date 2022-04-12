from collections import defaultdict


n = int(input())
colors = defaultdict(int)
for _ in range(n):
	d, a = map(int, input().split())
	colors[d] += a

answer = list()
for color in sorted(colors.items()):
	answer.append(' '.join(map(str, color)))
print('\n'.join(answer))
