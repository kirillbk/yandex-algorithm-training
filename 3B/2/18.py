# 16. Очередь с защитой от ошибок

from collections import deque
from sys import stdin
# 18. Дек с защитой от ошибок

d = deque()
result = list()
for line in stdin:
	cmd = line.split()
	if cmd[0] == 'push_back':
		d.append(int(cmd[1]))
		result.append('ok')
	elif cmd[0] == 'push_front':
		d.appendleft(int(cmd[1]))
		result.append('ok')
	elif cmd[0] == 'pop_front':
		if d:
			result.append(d.popleft())
		else:
			result.append('error')
	elif cmd[0] == 'pop_back':
		if d:
			result.append(d.pop())
		else:
			result.append('error')
	elif cmd[0] == 'front':
		if d:
			result.append(d[0])
		else:
			result.append('error')
	elif cmd[0] == 'back':
		if d:
			result.append(d[-1])
		else:
			result.append('error')
	elif cmd[0] == 'size':
		result.append(len(d))
	elif cmd[0] == 'clear':
		d.clear()
		result.append('ok')
	else:
		result.append('bye')
		break
print(*result, sep='\n')
