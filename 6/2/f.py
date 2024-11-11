# F. Сумма тройных произведений

M = 1000000007

n = int(input())
a = map(int, input().split())
a = list(a)

sum_pref = [0] * (n + 1)
for i in range(1, n + 1):
    sum_pref[i] = sum_pref[i - 1] + a[i - 1]
    sum_pref[i] %= M

mul_pref = [0] * (n + 1)
for i in range(1, n + 1):
    mul_pref[i] = mul_pref[i - 1] + (a[i - 1] * (sum_pref[-1] - sum_pref[i])) % M
    mul_pref[i] %= M

ans = 0
for i in range(n - 2):
    ans += a[i] * (mul_pref[-1] - mul_pref[i + 1])
    ans %= M

print(ans)
