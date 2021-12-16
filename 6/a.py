# A. Двоичный поиск
# Реализуйте двоичный поиск в массиве

# Формат ввода
# В первой строке входных данных содержатся натуральные числа N и K (0 > N, K <= 100000).
# Во второй строке задаются N элементов первого массива, а в третьей строке – K элементов второго массива.
# Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит 10^9

# Формат вывода
# Требуется для каждого из K чисел вывести в отдельную строку "YES", если это число встречается в первом массиве, и "NO" в противном случае.

def find(num, array):
	left = 0
	right = len(array) - 1
	while left < right:
		m = (left + right) // 2
		if num > array[m]:
			left = m + 1
		else:
			right = m
	return array[left] == num

n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for num in list2:
	if find(num, list1):
		print('YES')
	else:
		print('NO')
