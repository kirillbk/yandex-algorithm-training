# 2. Красивая строка

from string import ascii_lowercase


k = int(input())
s = input()

answer = 0
for char in ascii_lowercase:
	substitutions = 0
	r = 0
	for l in range(len(s)):
		while r < len(s) and (s[r] == char or substitutions < k):
			if s[r] != char:
				substitutions += 1
			r += 1
		answer = max(answer, r - l)
		if s[l] != char:
			substitutions -= 1
		if r == len(s):
			break

print(answer)
