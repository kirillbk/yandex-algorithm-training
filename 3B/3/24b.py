# 24. Покупка билетов

A = 0
B = 1
C = 2

n = int(input())
abc = [None] * (n+3)
abc[0] = abc[-1] = abc[-2] = float('inf'), float('inf'), float('inf')
for i in range(1, n+1):
	a, b, c = map(int, input().split())
	abc[i] = a, b, c

dp = [0] * (n+3)
for i in range(1, n+1):
	"""
	i-й человек в очереди:
		- сам купил себе билет
		- i - 1 купил ему билет
		- i - 2 купил билеты i и i - 1
	"""
	dp[i] = min(dp[i-1] + abc[i][A], dp[i-2] + abc[i-1][B], dp[i-3] + abc[i-2][C])

print(dp[n])

