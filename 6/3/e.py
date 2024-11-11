# E. Значение арифметического выражения

from re import findall


def get_postfix(s: str) -> list[str | None] | None:
    postfix = []
    stack = []
    for token in findall(r"\d+|[\+\-\*()]|\S", s):
        match token:
            case "+" | "-":
                while stack and stack[-1] in "+-*":
                    postfix.append(stack.pop())
                stack.append(token)
            case "*":
                while stack and stack[-1] == "*":
                    postfix.append(stack.pop())
                stack.append(token)
            case "(":
                stack.append(token)
            case ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                if not stack or stack[-1] != "(":
                    return None
                stack.pop()
            case _:
                try:
                    postfix.append(int(token))
                except ValueError:
                    return None

    while stack and stack[-1] in "+-*":
        postfix.append(stack.pop())

    return postfix if not stack else None


def calc_postfix(postfix: list[str, int]) -> int | None:
    stack = []
    for op in postfix:
        if isinstance(op, int):
            stack.append(op)
        else:
            try:
                b = stack.pop()
                a = stack.pop()
            except IndexError:
                return None
            match op:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case _:
                    raise RuntimeError()

    return stack[0] if len(stack) == 1 else None


def solution(s: str) -> str:
    postfix = get_postfix(s)
    if not postfix:
        return "WRONG"
    ans = calc_postfix(postfix)
    if ans is None:
        return "WRONG"
    return str(ans)


s = input()
print(solution(s))
