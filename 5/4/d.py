# D. Рапорт

def get_height(a: list[int], l: int, r: int):
    i = 0
    line = 1
    width = r - l

    for length in a:
        if i + length > width:
            line += 1
            i = length + 1
        else:
            i += length + 1

    return line


w, n, m = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

l = max(a)
r = w - max(b)
while r - l > 1:
    m = (l + r) // 2
    a_heihgt = get_height(a, 0, m)
    b_height = get_height(b, m, w)
    if a_heihgt < b_height:
        r = m
    else:
        l = m

h1 = max(
    get_height(a, 0, l),
    get_height(b, l, w)
)
h2 = max(
    get_height(a, 0, r),
    get_height(b, r, w)
)
print(min(h1, h2))
