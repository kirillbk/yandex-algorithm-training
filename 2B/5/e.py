def solution(a, b, c, s):
	c_dict = dict()
	for k in range(len(c)):
		c_k = c[k]
		if c_k not in c_dict:
			c_dict[c_k] = k
	for i in range(len(a)):
		for j in range(len(b)):
			c_k = s - (a[i] + b[j])
			k = c_dict.get(c_k, -1)
			if k != -1:
				return i, j, k
	return -1,

# Решение без словаря
# def solution(a, b, c, s):
# 	a = [(a[i], i) for i in range(len(a))]
# 	b = [(b[i], i) for i in range(len(b))]
# 	c = [(c[i], i) for i in range(len(c))]
# 	a.sort()
# 	b.sort()
# 	c.sort(key=lambda x: (x[0], -x[1]))
# 	answer = None
# 	for a_i, i in a:
# 		c_pos = len(c) - 1
# 		for b_j, j in b:
# 			while c_pos >= 0 and a_i + b_j + c[c_pos][0] > s:
# 				c_pos -= 1
# 			if c_pos < 0:
# 				break
# 			if a_i + b_j + c[c_pos][0] == s and (answer == None or (i, j, c[c_pos][0]) < answer):
# 				answer = i, j, c[c_pos][1]
# 	if answer:
# 		return answer
# 	return -1,


s = int(input())
a = list(map(int, input().split()[1:]))
b = list(map(int, input().split()[1:]))
c = list(map(int, input().split()[1:]))

print(*solution(a, b, c, s))
