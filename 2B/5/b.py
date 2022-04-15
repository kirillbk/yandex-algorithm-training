n = int(input())
a = list(map(int, input().split()))

answer = a[0]
sum = 0
for i in range(n):
	sum += a[i]
	answer = max(sum, answer)
	if sum < 0:
		sum = 0

# answer = a[0]
# sum = 0
# min_sum = 0
# for i in range(n):
# 	sum += a[i]
# 	answer = max(answer, sum - min_sum)
# 	min_sum = min(sum, min_sum)

print(answer)

