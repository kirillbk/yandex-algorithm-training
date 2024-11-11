# D. Постфиксная запись

s = input()

stack = []
for arg in s.split():
    try:
        stack.append(int(arg))
    except ValueError:
        b = stack.pop()
        a = stack.pop()
        match arg:
            case "+":
                stack.append(a + b)
            case "-":
                stack.append(a - b)
            case "*":
                stack.append(a * b)
            case _:
                raise RuntimeError()

print(stack[0])
