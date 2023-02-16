# 13. Постфиксная запись

expression = input().split()

stack = list()
for item in expression:
	if item.isdigit():
		stack.append(int(item))
	else:
		b = stack.pop()
		a = stack.pop()
		if item == '+':
			stack.append(a + b)
		elif item == '-':
			stack.append(a - b)
		else:
			stack.append(a * b)

print(stack[0])
