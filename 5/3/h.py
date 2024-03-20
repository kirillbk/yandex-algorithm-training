# H. Спички детям не игрушка!

from collections import defaultdict
from dataclasses import dataclass
from typing import Any


@dataclass
class Point:
    x: int
    y: int


@dataclass(init=False)
class Match:
    a: Point
    b: Point

    def __init__(self, x1, y1, x2, y2) -> None:
        if x1 > x2 or x1 == x2 and y1 > y2:
            x1, y1, x2, y2 =  x2, y2, x1, y1
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Match):
            raise NotImplementedError
        return (
            self.b.x - self.a.x == other.b.x - other.a.x
            and self.b.y - self.a.y == other.b.y - other.a.y
        )

    def translate(self, other: Any) -> tuple[int, int] | None:
        if not isinstance(other, Match):
            raise NotImplementedError
        if self != other:
            return None
        return other.a.x - self.a.x, other.a.y - self.a.y


n = int(input())
source = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    source.append(Match(x1, y1, x2, y2))
dest = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    dest.append(Match(x1, y1, x2, y2))

cntr = defaultdict(int)
for match_a in source:
    for match_b in dest:
        v = match_a.translate(match_b)
        if v:
            cntr[v] += 1

max_translated = 0
if cntr:
    max_translated = max(cntr.values())
print(n - max_translated)
