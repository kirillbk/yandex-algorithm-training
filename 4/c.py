# C. Самое частое слово
# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# Формат ввода
# Вводится текст.

# Формат вывода
# Выведите ответ на задачу.

from sys import stdin

word_freq = {}
max_freq = 0
result = ''
for word in stdin.read().split():
	if word not in word_freq:
		word_freq[word] = 0
	word_freq[word] += 1
	if word_freq[word] > max_freq or word_freq[word] == max_freq and word < result:
		result = word
		max_freq = word_freq[word]

print(result)
