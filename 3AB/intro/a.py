# Андрей и кислота

def solution(a, n):
	for i in range(n - 2, -1, -1):
		if a[i] > a[i + 1]:
			return -1
	return a[-1] - a[0]


n = int(input())
a = list(map(int, input().split()))
print(solution(a, n))
