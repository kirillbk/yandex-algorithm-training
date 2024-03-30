# C. Саруман

n, m = map(int, input().split())
a = [*map(int, input().split())]

p_sum = [0] * (n + 1)
p_sum[0] = 0
for i in range(1, n + 1):
    p_sum[i] = p_sum[i - 1] + a[i - 1]

answer = []
for _ in range(m):
    length, s = map(int, input().split())

    left = 0
    right = n - length + 1
    while right - left > 1:
        m = (right + left) // 2
        if p_sum[m + length] - p_sum[m] > s:
            right = m
        else:
            left = m

    if p_sum[left + length] - p_sum[left] == s:
        answer.append(left + 1)
    else:
        answer.append(-1)

print(*answer, sep='\n')
