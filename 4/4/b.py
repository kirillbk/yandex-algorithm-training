# B. Затерянный мир

class Solver:
    def __init__(self, n: int) -> None:
        self._n = n
        self._rows = [False] * n
        self._down = [False] * (2 * n - 1)
        self._up = [False] * (2 * n - 1)
        self._answer = 0

    def _add_queen(self, x: int, y: int) -> bool:
        if self._rows[y] or self._up[x + y] or self._down[self._n - 1 - (x - y)]:
            return False
        self._rows[y] = True
        self._up[x + y] = True
        self._down[self._n - 1 - (x - y)] = True
        return True

    def _remove_queen(self, x: int, y: int):
        self._rows[y] = False
        self._up[x + y] = False
        self._down[self._n - 1 - (x - y)] = False


    def _solve(self, queens: int, x: int):
        if queens == 0:
            self._answer += 1
            return
        for y in range(self._n):
            if self._add_queen(x, y):
                self._solve(queens - 1, x + 1)
                self._remove_queen(x, y)

    def solve(self) -> int:
        self._solve(self._n, 0)
        return self._answer


n = int(input())

solver = Solver(n)
print(solver.solve())
