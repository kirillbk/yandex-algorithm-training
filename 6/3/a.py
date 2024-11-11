# A. Правильная скобочная последовательность


def solution(s: str) -> bool:
    closed = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for b in s:
        if b in closed:
            stack.append(closed[b])
        elif stack and stack[-1] == b:
            stack.pop()
        else:
            return False

    if stack:
        return False
    return True


s = input()
print("yes" if solution(s) else "no")
