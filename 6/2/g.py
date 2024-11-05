# G. Цензурное произведение

n, c = map(int, input().split())
s = input()

ans = 0
rudeness = 0
a_cntr = b_cntr = 0
l = 0
for r in range(n):
    if s[r] == "b":
        rudeness += a_cntr
        b_cntr += 1
    elif s[r] == "a":
        a_cntr += 1

    while l < r and rudeness > c:
        if s[l] == "a":
            rudeness -= b_cntr
            a_cntr -= 1
        elif s[l] == "b":
            b_cntr -= 1
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
