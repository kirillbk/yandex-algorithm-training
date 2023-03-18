# 16. Очередь с защитой от ошибок

from collections import deque
from sys import stdin


queue = deque()
result = list()
for line in stdin:
	cmd = line.split()
	if cmd[0] == 'push':
		queue.append(int(cmd[1]))
		result.append('ok')
	elif cmd[0] == 'pop':
		if queue:
			result.append(queue.popleft())
		else:
			result.append('error')
	elif cmd[0] == 'front':
		if queue:
			result.append(queue[0])
		else:
			result.append('error')
	elif cmd[0] == 'size':
		result.append(len(queue))
	elif cmd[0] == 'clear':
		queue.clear()
		result.append('ok')
	else:
		result.append('bye')
		break
print(*result, sep='\n')
