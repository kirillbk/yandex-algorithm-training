# 29. Кафе

n = int(input())
prices = [0] * (n + 1)
for i in range(1, n + 1):
	prices[i] = int(input())

'''
	строки(i) - дни
	стобцы(j) - количество купонов
	dp[i][j] - сумма потраченная на обеды за i дней, имеется j купонов
'''
dp = [[0] * (n + 2) for _ in range(n + 1)]
for i in range(1, n + 2):
	dp[0][i] = float('inf')
for i in range(1, n + 1):
	dp[i][-1] = float('inf')
for i in range(1, n + 1):
	for j in range(0, n + 1):
		# купить обед (получить купон, если он стоил более 100) или потратить купон
		if prices[i] > 100:
			dp[i][j] = min(dp[i-1][j-1] + prices[i], dp[i-1][j+1])
		else:
			dp[i][j] = min(dp[i-1][j] + prices[i], dp[i-1][j+1])

coupons = min(dp[n])
for i in range(n, -1, -1):
	if dp[n][i] == coupons:
		k1 = i
		break
k2 = 0
j = k1
answer = list()
for i in range(n, 1, -1):
	if dp[i][j] == dp[i - 1][j] + prices[i]:
		pass
	elif dp[i][j] == dp[i-1][j-1] + prices[i]:
		j -= 1
	else:
		k2 += 1
		answer.append(i)
		j += 1

print(coupons)
print(k1, k2)
print(*reversed(answer), sep='\n')
