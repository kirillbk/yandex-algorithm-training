# F. Велодорожки

def build_road(
    tiles: list[int, int],
    n: int,
    width: int,
    max_pref: list[int],
    min_pref: list[int],
    max_suff: list[int],
    min_suff: list[int]
) -> bool:
    r = 0
    for l in range(n):
        while r < n and tiles[r][0] - tiles[l][0] < width:
            r += 1

        y1 = min(min_pref[l], min_suff[r])
        y2 = max(max_pref[l], max_suff[r])
        if y2 - y1 < width:
            return True

    return False


w, h, n = map(int, input().split())
tiles = []
for _ in range(n):
    x, y = map(int, input().split())
    tiles.append((x, y))

tiles.sort()
max_prefix = [0] * (n + 1)
min_prefix = [10**9 + 1] * (n + 1)
for i in range(1, n + 1):
    max_prefix[i] = max(max_prefix[i - 1], tiles[i - 1][1])
    min_prefix[i] = min(min_prefix[i - 1], tiles[i - 1][1])

max_suffix = [0] * (n + 1)
min_suffix = [10**9 + 1] * (n + 1)
for i in range(n - 1, -1, -1):
    max_suffix[i] = max(max_suffix[i + 1], tiles[i][1])
    min_suffix[i] = min(min_suffix[i + 1], tiles[i][1])

l = 0
r = min(w, h)
while r - l > 1:
    m = (l + r) // 2
    if build_road(
        tiles, n, m,
        max_prefix,
        min_prefix,
        max_suffix,
        min_suffix
    ):
        r = m
    else:
        l = m

print(r)
