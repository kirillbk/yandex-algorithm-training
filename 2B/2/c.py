str = input()

answer = 0
i = 0
j = len(str) - 1
while(i < j):
	if str[i] != str[j]:
		answer += 1
	i += 1
	j -= 1

print(answer)
