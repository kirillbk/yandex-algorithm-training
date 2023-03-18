# 28. Космический мусорщик

from collections import Counter
from copy import copy

mapping = str.maketrans('NSWEUD', '012345')
rules = list()
for _ in range(6):
	rule = map(int, input().translate(mapping))
	rules.append(Counter(rule))
cmd, m = input().split()
cmd = int(cmd.translate(mapping))
m = int(m)

# dp[i] = количество перемещений для команды i c параметром m
dp = [1] * 6
for _ in range(1, m):
	next_dp = [1] * 6
	for j in range(6):
		for command, n in rules[j].items():
			next_dp[j] += dp[command] * n
	dp = next_dp

print(dp[cmd])

