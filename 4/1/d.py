# D. Сортировка слиянием

def merge(
        a: list,
        l: int,
        m: int,
        r: int,
        res: list,
        i: int
    ):
    idx1 = l
    idx2 = m

    while idx1 < m and idx2 < r:
        if a[idx2] < a[idx1]:
            res[i] = a[idx2]
            idx2 += 1
        else:
            res[i] = a[idx1]
            idx1 += 1
        i += 1

    while idx1 < m:
        res[i] = a[idx1]
        idx1 += 1
        i += 1
    while idx2 < r:
        res[i] = a[idx2]
        idx2 += 1
        i += 1


def _merge_sort(
        a: list,
        left: int,
        right: int,
        buffer: list,
    ):
    if right - left <= 1:
        return

    middle = (left + right) // 2
    _merge_sort(a, left, middle, buffer)
    _merge_sort(a, middle, right, buffer)
    merge(a, left, middle, right, buffer, left)

    for i in range(left, right):
        a[i] = buffer[i]


def merge_sort(array: list, n: int) -> list:
    buffer = [None] * n
    _merge_sort(array, 0, n, buffer)


n = int(input())
a = list(map(int, input().split()))
merge_sort(a, n)
print(*a)
