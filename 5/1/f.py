# F. Миша и математика

n = int(input())
a = list(map(int, input().split()))

answer = ['+'] * (n - 1)
odd_cntr = sum(1 for i in range(n) if a[i] % 2 != 0)
if odd_cntr % 2 == 0:
    for i in range(n - 1):
        if a[i] % 2 != 0:
            answer[i] = 'x'
            break

print(''.join(answer))
