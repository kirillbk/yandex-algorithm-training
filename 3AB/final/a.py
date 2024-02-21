# A. Подземная доставка

from collections import defaultdict


n = int(input())
train = list()
items = defaultdict(int)
for _ in range(n):
	cmd = input().split()
	if cmd[0] == 'add':
		qty = int(cmd[1])
		train.append([cmd[2], qty])
		items[cmd[2]] += qty
	elif cmd[0] == 'delete':
		qty = int(cmd[1])
		while train and qty >= train[-1][1]:
			qty -= train[-1][1]
			items[train[-1][0]] -= train[-1][1]
			train.pop()
		if train:
			items[train[-1][0]] -= qty
			train[-1][1] -= qty
	else:
		print(items[cmd[1]])
