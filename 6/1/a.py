# A. Плот


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

ans = ""
if y > y2:
    ans += "N"
if y < y1:
    ans += "S"
if x < x1:
    ans += "W"
if x > x2:
    ans += "E"

print(ans)
