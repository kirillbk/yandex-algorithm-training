# B. Приближенный двоичный поиск
# Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.

# Формат ввода
# В первой строке входных данных содержатся числа N и K ((0 > N, K < 100001)). Во второй строке задаются N чисел первого массива, отсортированного по неубыванию, а в третьей строке – K чисел второго массива. Каждое число в обоих массивах по модулю не превосходит 2*10^9.

# Формат вывода
# Для каждого из K чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких несколько, выведите меньшее из них.

def find(num, data):
	left = 0
	right = len(data) - 1
	while left < right:
		m = (left + right) // 2
		if num > data[m]:
			left = m + 1
		else:
			right = m
	if data[left] != num and left != 0  and abs(data[left - 1] - num) <= abs(data[left] - num):
		left -= 1
	return data[left]

n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for num in list2:
	print(find(num, list1))
