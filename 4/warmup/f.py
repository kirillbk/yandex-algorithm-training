# F. Лифт

k = int(input())
n = int(input())
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(input())

answer = 0
lift = 0
top_flat = 0
for i in range(n, 0, -1):
    # полные лифты, которые нужно отправить на этаж
    answer += a[i] // k * 2 * i
    # сотрудники, которые останутся на этаже, после того, как уедут полные лифты
    employees = a[i] % k
    if employees == 0:
        continue
    top_flat = max(top_flat, i)
    # все сотрудники на этаже поместятся в лифт, идущий сверху
    if employees < k - lift:
        lift += employees
    # количество свободных мест в лифте меньше или равно количеству сотрудников на этаже
    else:
        lift = employees - (k - lift)
        answer += top_flat * 2
        top_flat = i if lift !=0 else 0
answer += top_flat * 2

print(answer)
