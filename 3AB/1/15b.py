# 15. Великое Лайнландское переселение

n = int(input())
a = list(map(int, input().split()))

stack = list()
answer = [-1] * n
for i in range(n):
	while stack and stack[-1][0] > a[i]:
		item = stack.pop()
		answer[item[1]] = i
	stack.append((a[i], i))

print(*answer)
