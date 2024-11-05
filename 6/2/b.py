# B. Сумма номеров

n, k = map(int, input().split())
a = map(int, input().split())
a = list(a)

ans = 0
prefix_set = set()
now_prefix = 0
prefix_set.add(now_prefix)
for num in a:
    now_prefix = now_prefix + num
    prefix_set.add(now_prefix)
    if now_prefix - k in prefix_set:
        ans += 1

print(ans)
