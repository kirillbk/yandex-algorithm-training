# 12. Значение арифметического выражения

from re import findall
from typing import List


def to_postfix(expression: str) -> List[str] | None:
	tokens = findall(r'\d+|[\+\-\*\(\)]|[a-zA-Z]', expression)
	balance = 0
	postfix = list()
	stack = list()

	for token in tokens:
		if token.isdigit():
			postfix.append(token)
		elif token == '(':
			balance += 1
			stack.append(token)
		elif token in '+-':
			while stack and stack[-1] in '+-*':
				postfix.append(stack.pop())
			stack.append(token)
		elif token in '*':
			while stack and stack[-1] in '*':
				postfix.append(stack.pop())
			stack.append(token)
		elif token == ')':
			balance -= 1
			if balance < 0:
				return None
			while stack and stack[-1] in '+-*':
				postfix.append(stack.pop())
			stack.pop()
		else:
			return None

	while stack and stack[-1] in '+-*':
		postfix.append(stack.pop())

	if balance != 0 or stack:
		return None
	return postfix


def calculate(postfix: List[str]) -> str:
	if not postfix:
		return 'WRONG'

	stack = list()

	for item in postfix:
		if item not in '+-*':
			stack.append(int(item))
			continue
		try:
			b = stack.pop()
			a = stack.pop()
		except IndexError as e:
			return 'WRONG'
		if item == '+':
			stack.append(a + b)
		elif item == '-':
			stack.append(a - b)
		else:
			stack.append(a * b)


	if len(stack) != 1:
		return 'WRONG'
	return str(stack[0])


postfix = to_postfix(input())
print(calculate(postfix))

