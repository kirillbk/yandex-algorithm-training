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

    def translate(self, other: Any) -> Point | None:
        if not isinstance(other, Match):
            raise NotImplementedError
        va = self.a.x - other.a.x, self.a.y - other.a.y
        vb = self.b.x - other.b.x, self.b.y - other.b.y
        if va != vb:
            return None
        return va


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
