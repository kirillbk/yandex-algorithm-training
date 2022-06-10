def f(a, b, c, d, x):
	return a * pow(x, 3) + b * pow(x, 2) + c * x + d


a, b, c, d = map(int, input().split())

l = -1
r = 1
# найдём границы поиска
# если произведение f(l) * f(r) <= 0, то корень уравнения на этом отрезке
while f(a, b, c, d, l) * f(a, b, c, d, r) > 0:
	l *= 2
	r *= 2

# решение с точностью 1e-5 (10^-5)
while r - l > 1e-5:
	m = (l + r) / 2
	if m == l or m == r:
		break
	# проверим, есть ли корень уравнения на отрезке [m, r]
	if f(a, b, c, d, m) * f(a, b, c, d, r) > 0:
		r = m
	else:
		l = m

# # решение за 100 итераций без точности
# for i in range(100):
# 	m = (r + l) / 2
# 	if f(a, b, c, d, m) * f(a, b, c, d, r) > 0:
# 		r = m
# 	else:
# 		l = m

# ответ в l, т. к. f(m) * f(r) <= 0
print(l)
