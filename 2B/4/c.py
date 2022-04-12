from collections import Counter
from sys import stdin

word_freq = Counter(stdin.read().split())
answer = sorted(word_freq.items(), key=lambda x:(-x[1], x[0]))

print('\n'.join(word for word, _ in answer))
