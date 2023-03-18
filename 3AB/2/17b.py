# 17. Игра в пьяницу

from collections import deque


first = deque(map(int, input().split()))
second = deque(map(int, input().split()))
for i in range(10**6):
	card1 = first.popleft()
	card2 = second.popleft()
	if card1 == 0 and card2 == 9:
		winner = first
	elif card2 == 0 and card1 == 9:
		winner = second
	elif card1 > card2:
		winner = first
	else:
		winner = second
	winner.append(card1)
	winner.append(card2)
	if not first:
		print('second', i + 1)
		break
	if not second:
		print('first', i + 1)
		break
else:
	print('botva')
