# J. Два прямоугольника

from dataclasses import dataclass


@dataclass
class Rectangle:
    x0: int
    y0: int
    x1: int
    y1: int

    @property
    def area(self) -> int:
        a = self.x1 - self.x0 + 1
        b = self.y1 - self.y0 + 1
        return a * b

    def expand(self, picture: list[list[str]], n: int, m: int, filler: str):
        x = self.x0 + 1
        while x < m and picture[self.y0][x] == '#':
            picture[self.y0][x] = filler
            x += 1
        self.x1 = x - 1

        y = self.y0 + 1
        while y < n and picture[y][self.x0] == '#':
            x = self.x0 + 1
            while x < m and x < self.x1 + 1 and picture[y][x] == '#':
                x += 1
            left_area = self.x0 > 0 and picture[y][self.x0 - 1] == '#'
            right_area = self.x1 < m - 1 and picture[y][self.x1 + 1] == '#'
            if x - 1 != self.x1 or left_area and right_area:
                break
            for i in range(self.x0, x):
                    picture[y][i] = filler
            y += 1
        self.y1 = y - 1

    def split(self, picture: list[list[str]], n: int, m: int, filler: str):
        if self.x0 == self.x1 or self.y0 == self.y1:
            picture[self.y1][self.x1] = filler
        else:
            for x in range(self.x0, self.x1 + 1):
                picture[self.y1][x] = filler


def find_two_rectangles(picture: list[list[str]], n: int, m: int) -> list[Rectangle]:
    filler = 'a'
    rectangles = []

    for y in range(n):
        for x in range(m):
            if picture[y][x] == '#':
                picture[y][x] = filler
                r = Rectangle(x, y, x, y)
                r.expand(picture, n, m, filler)

                filler = 'b'
                rectangles.append(r)
                if len(rectangles) == 2:
                    return rectangles

    return rectangles


def solution(picture: list[list[str]], n: int, m: int) -> bool:
    rectangles = find_two_rectangles(picture, n, m)

    if len(rectangles) == 0:
        return False

    if len(rectangles) == 1:
        if rectangles[0].area == 1:
            return False
        rectangles[0].split(picture, n, m, 'b')

    for y in range(n):
        for x in range(m):
            if picture[y][x] == '#':
                return False

    return True


n, m = map(int, input().split())
picture = []
for _ in range(n):
    picture.append([*input()])

if solution(picture, n, m):
    print('YES')
    for line in picture:
        print(*line, sep='')
else:
    print('NO')
