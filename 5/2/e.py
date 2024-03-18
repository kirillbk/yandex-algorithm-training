# E. Амбициозная улитка

n = int(input())
berries = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    berries[i] = a, b

# индексы ягод с подъёмом
left = []
# индексы ягод со спуском
right = []
# ягода с максимальным b среди ягод с подъёмом(b, индекс)
asc_b = -1
last_asc = - 1
# ягода с максимальным a среди ягод со спуском(a, индекс)
desc_a = -1
first_desc = -1
# высота после всех ягод с подъёмом
height = 0
for i in range(n):
    a, b = berries[i]
    if a > b:
        left.append(i)
        height += a - b
        if b > asc_b:
            asc_b = b
            last_asc = i
    else:
        right.append(i)
        if a > desc_a:
            desc_a = a
            first_desc = i

if (first_desc == -1
    or
    last_asc != -1 and height + berries[last_asc][1] > height + berries[first_desc][0]
):
    height += asc_b
    left.remove(last_asc)
    left.append(last_asc)
else:
    height += desc_a
    right.remove(first_desc)
    left.append(first_desc)
left.extend(right)

print(height)
print(*(i + 1 for i in left))
