from collections import Counter
from sys import stdin

word_freq = Counter(stdin.read().split())
answer = [(freq, word) for word, freq in word_freq.items()]
answer.sort(key=lambda x:(-x[0], x[1]))

print('\n'.join(word for _, word in answer))
