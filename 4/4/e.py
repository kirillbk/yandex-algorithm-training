# E. Генерация правильных скобочных последовательностей - 2

def solution(n: int, sequence: str, stack: list[str]):
    if len(sequence) == n:
        print(sequence)
        return

    if n - len(sequence) > len(stack):
        for b in '([':
            stack.append(b)
            solution(n , sequence + b, stack)
            stack.pop()
    if stack:
        tmp = stack[-1]
        stack.pop()
        b = ')' if tmp == '(' else ']'
        solution(n, sequence + b, stack)
        stack.append(tmp)


n = int(input())
if n % 2 == 0:
    solution(n, '', [])
