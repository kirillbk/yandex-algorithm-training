# H. Подстрока
# В этой задаче Вам требуется найти максимальную по длине подстроку данной строки, такую что каждый символ встречается в ней не более k раз.

# Формат ввода
# В первой строке даны два целых числа n и k (1 ≤ n ≤ 100000, 1 ≤ k ≤ n ) , где n – количество символов в строке. Во второй строке n символов – данная строка, состоящая только из строчных латинских букв.

# Формат вывода
# В выходной файл выведите два числа – длину искомой подстроки и номер её первого символа. Если решений несколько, выведите любое.

from collections import defaultdict

n, k = map(int, input().split())
s = input()

counter = defaultdict(int)
substr_strart = 1
substr_len = 0
left = right = 0
for right in range(n):
	# добавить к счётчику очередной символ
	counter[s[right]] += 1
	# пока количество очередных символов больше k, двигать левую границу
	while counter[s[right]] > k:
		counter[s[left]] -= 1
		left += 1
	if right - left + 1 > substr_len:
		substr_strart = left + 1
		substr_len = right - left + 1

print(substr_len, substr_strart)
