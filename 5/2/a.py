# A. Минимальный прямоугольник

k = int(input())
x = []
y = []
for _ in range(k):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

x0, y0 = min(x), min(y)
x1, y1 = max(x), max(y)

print(x0, y0, x1, y1)
