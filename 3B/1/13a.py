# 13. Значение логического выражения

from typing import List

def to_postfix(expression: str) -> List[str]:
	postfix = list()
	stack = list()

	for item in expression:
		if item.isdigit():
			postfix.append(item)
		elif item == '!':
			while stack and stack[-1] in '!':
				postfix.append(stack.pop())
			stack.append(item)
		elif item == '&':
			while stack and stack[-1] in '&!':
				postfix.append(stack.pop())
			stack.append(item)
		elif item in '|^':
			while stack and stack[-1] in '|^!&':
				postfix.append(stack.pop())
			stack.append(item)
		elif item == '(':
			stack.append(item)
		else:
			while stack and stack[-1] in '!&|^':
				postfix.append(stack.pop())
			stack.pop()

	while stack:
		postfix.append(stack.pop())

	return postfix


def calculate(postfix: List[str]) -> int:
	operations = {
		'&': lambda a, b: a & b,
		'|': lambda a, b: a | b,
		'^': lambda a, b: a ^ b
	}
	stack = list()

	for item in postfix:
		if item.isdigit():
			stack.append(int(item))
		elif item == '!':
			a = stack.pop()
			stack.append(0 if a == 1 else 1)
		else:
			b = stack.pop()
			a = stack.pop()
			result = operations[item](a, b)
			stack.append(result)

	return stack[0]


postfix = to_postfix(input())
print(calculate(postfix))
