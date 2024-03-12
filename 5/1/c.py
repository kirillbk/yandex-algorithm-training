# C. Форматирование файла

n = int(input())
answer = 0
for _ in range(n):
    a = int(input())
    answer += a // 4
    a %= 4
    if a > 1:
        answer += 2
    elif a == 1:
        answer += 1

print(answer)
