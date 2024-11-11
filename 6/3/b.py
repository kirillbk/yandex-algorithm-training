# B. Великое Лайнландское переселение

n = int(input())
a = map(int, input().split())
a = list(a)

ans = [-1] * n
stack = [(0, a[0])]
for i in range(1, n):
    while stack and a[i] < stack[-1][1]:
        j, _ = stack.pop()
        ans[j] = i
    stack.append((i, a[i]))

print(*ans)
