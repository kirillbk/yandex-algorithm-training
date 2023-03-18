# 11. Стек с защитой от ошибок

from sys import stdin

stack = list()
for line in stdin:
	cmd = line.split()
	if cmd[0] == 'push':
		stack.append(cmd[1])
		print('ok')
	elif cmd[0] == 'pop':
		if stack:
			print(stack.pop())
		else:
			print('error')
	elif cmd[0] == 'back':
		if stack:
			print(stack[-1])
		else:
			print('error')
	elif cmd[0] == 'size':
		print(len(stack))
	elif cmd[0] == 'clear':
		stack.clear()
		print('ok')
	else:
		print('bye')
		break
