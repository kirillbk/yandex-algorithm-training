# 1. Гистограмма

from collections import Counter
from sys import stdin
from string import whitespace


text = Counter(stdin.read())
for space in whitespace:
	text.pop(space, None)
symbols = sorted(text.keys())
top = max(text.values())
answer = list()
for i in range(top, 0, -1):
	line = (' ' if text[s] < i else '#' for s in symbols)
	answer.append(''.join(line))
answer.append(''.join(symbols))
print(*answer, sep='\n')
