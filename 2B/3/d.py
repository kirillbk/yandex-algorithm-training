n = int(input())
answer = set(i for i in range(1, n + 1))
while True:
	question = input()
	if question == 'HELP':
		break
	question = map(int, question.split())
	if input() == 'YES':
		answer.intersection_update(question)
	else:
		answer.difference_update(question)

print(*sorted(answer))
