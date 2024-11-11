# F. Минимальная ПСП

n = int(input())
w = input()
s = input()

stack = []
for b in s:
    if b in "([":
        stack.append(b)
    else:
        stack.pop()

while len(s) < n:
    for b in w:
        if b in "([" and len(stack) + 2 <= n - len(s):
            stack.append(b)
            s += b
            break
        elif stack and (b == ")" and stack[-1] == "(" or b == "]" and stack[-1] == "["):
            stack.pop()
            s += b
            break

print(s)
