# 12. Правильная скобочная последовательность

def is_valid(s: str) -> bool:
	stack = list()
	pairs = {')': '(', '}': '{', ']': '['}

	for bracket in s:
		if bracket in pairs:
			if not stack or stack[-1] != pairs[bracket]:
				return False
			stack.pop()
		else:
			stack.append(bracket)
	return not stack

s = input()
if is_valid(s):
	print('yes')
else:
	print('no')

