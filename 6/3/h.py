# H. Стек с суммой


class Stack:
    def __init__(self) -> None:
        self._data: list[int] = []
        self._prefix: list[int] = [0]

    def push(self, x: int) -> int:
        if not isinstance(x, int):
            raise TypeError(f"integer number expected, got {type(x).__name__}")
        self._data.append(x)
        self._prefix.append(x + self._prefix[-1])

        return x

    def pop(self) -> int:
        self._prefix.pop()

        return self._data.pop()

    def sum(self, k: int) -> int:
        if not isinstance(k, int):
            raise TypeError(f"integer number expected, got {type(x).__name__}")

        return self._prefix[-1] - self._prefix[-(k + 1)]


stack = Stack()
n = int(input())
for _ in range(n):
    op = input()
    if op.startswith("+"):
        stack.push(int(op[1:]))
    elif op.startswith("-"):
        print(stack.pop())
    elif op.startswith("?"):
        print(stack.sum(int(op[1:])))
    else:
        raise ValueError()
