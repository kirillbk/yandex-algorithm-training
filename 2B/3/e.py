m = int(input())
witnesses = [None] * m
for i in range(m):
	witnesses[i] = set(input())
n = int(input())
numbers = [[None, 0] for _ in range(n)]
max_matches = 0
for i in range(n):
	numbers[i][0] = input()
	number_set = set(numbers[i][0])
	for witness in witnesses:
		if witness.issubset(number_set):
			numbers[i][1] += 1
	if numbers[i][1] > max_matches:
		max_matches = numbers[i][1]

answer = (number[0] for number in numbers if number[1] == max_matches)
print('\n'.join(answer))
