from collections import defaultdict
from sys import stdin


total = defaultdict(int)
for line in stdin:
	if line == '':
		break
	candidate, votes = line.split()
	total[candidate] += int(votes)

answer = list()
for candidate in sorted(total.items()):
	answer.append(' '.join(map(str, candidate)))
print('\n'.join(answer))
