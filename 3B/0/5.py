# 5. Хорошая строка

n = int(input())
c = [0] * 26
for i in range(n):
	c[i] = int(input())

answer = 0
for i in range(n-1):
	answer += min(c[i], c[i+1])
print(answer)
