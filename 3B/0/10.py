# 10. Скучная лекция

from collections import defaultdict
s = input()
cntr = defaultdict(int)
for i in range(len(s)):
	n = (len(s) - i)*(i + 1)
	cntr[s[i]] += n
for char in sorted(cntr.keys()):
	print(f'{char}: {cntr[char]}')
