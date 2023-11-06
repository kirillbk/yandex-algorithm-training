# I. Правильная скобочная последовательность

def is_valid(s: str) -> bool:
    stack = list()
    opened = {"]": "[", "}" : "{", ")": "("}

    for c in s:
        if c in "[{(":
            stack.append(c)
        else:
            if not stack or stack[-1] != opened[c]:
                return False
            stack.pop()

    if stack:
        return False
    return True


s = input()

if is_valid(s):
    print("yes")
else:
    print("no")
