# 8. Минимальный прямоугольник

k = int(input())
x_coords = list()
y_coords = list()
for _ in range(k):
	x, y = map(int, input().split())
	x_coords.append(x)
	y_coords.append(y)
print(min(x_coords), min(y_coords), max(x_coords), max(y_coords))
