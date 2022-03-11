answer = 0
curr_max = 0

while(True):
	n = int(input())
	if n == 0:
		break
	elif n > curr_max:
		curr_max = n
		answer = 1
	elif n == curr_max:
		answer += 1
print(answer)
