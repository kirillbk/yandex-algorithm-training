# C. Туризм
# Александр недавно увлекся горным туризмом. Ему уже надоело покорять отдельные горные пики, и он собирается покорить самую настоящую горную цепь!
# Напомним, что Александр живет в плоском мире. Горная цепь состоит из отрезков, соединяющих точки на плоскости, каждая из которых находится строго правее предыдущей (x-координата следующей точки больше, чем у предыдущей). Трассой на горной цепи называется её часть между двумя фиксированными концами отрезков.
# Участок, на котором при движении по трассе координата y (высота) всегда возрастает, называется подъемом, величиной подъема называется разность высот между начальной и конечной точками участка.
# Туристическая компания предлагает на выбор несколько трасс на одной горной цепи. Александр из-за финансовых трудностей может выбрать для поездки только одну из этих трасс. Вы решили помочь ему с выбором. Александру важно для каждой трассы определить суммарную высоту подъемов на ней. Обратите внимание, что трасса может идти как слева-направо, так и справа-налево.

# Формат ввода
# В первой строке входного файла содержится единственное число N — количество точек ломаной, задающей горную цепь (1 ≤ N ≤ 30 000). Далее в N строках содержатся описания точек, каждое из которых состоит из двух целых чисел, xi и yi (1 ≤ xi, yi ≤ 30 000).
# В следующей строке находится число M — количество трасс (1 ≤ M ≤ 30 000).
# Далее в M строках содержатся описания трасс. Каждое описание представляет собой два целых числа, si и fi, они обозначают номера вершин начала и конца трассы, соответственно (1 ≤ si ≤ N, 1 ≤ fi ≤ N). Начало и конец трассы могут совпадать.
# Гарантируется, что во входном файле задана именно горная цепь.

# Формат вывода
# Для каждой трассы выведите одно число — суммарную высоту подъемов на данной трассе.

n = int(input())
peaks = []
for _ in range(n):
	x, y = map(int, input().split())
	peaks.append(y)
m = int(input())
routes = []
for _ in range(m):
	s, f = map(int, input().split())
	routes.append((s, f))

to_right = [0] * n
to_left = [0] * n
for i in range(1, n):
	to_right[i] = to_right[i - 1] + max(peaks[i] - peaks[i - 1], 0)
	to_left[n - i - 1] = to_left[n - i] + max(peaks[n - i - 1] - peaks[n - i], 0)

for route in routes:
	s, f = route[0] - 1, route[1] - 1
	if s < f:
		print(to_right[f] - to_right[s])
	else:
		print(to_left[f] - to_left[s])
