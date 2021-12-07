# H. Наибольшее произведение трех чисел
# В данном списке из n ≤ 105 целых чисел найдите три числа,произведение которых максимально.

# Решение должно иметь сложность O(n), где n - размер списка.

# Выведите три искомых числа в любом порядке.

# 3 максимума, 2 минимума.
# Максимальное произведение: max1 * max2 * max3 или max1 * min2 * min3 (по аналогии с задачей G)
# Можно отсортировать входной массив за O(nlogn)
# Решение из разбора O(n)

# На n-месте seq будет тот же элемент, что и в отсортированном массиве seq -  n-я порядковая статистика.
# Используется такой же алгоритм, как в быстрой сортировке, только для половины массива.
def	nth_rearrange(seq, begin, end, n):
	left = begin
	right = end - 1
	while left < right:
		# опорный элемент
		base = seq[(left + right) // 2]
		# индекс начала элементов больше опорного
		gt_base = left
		# индекс начала элементов равных опорному
		eq_base = left
		for i in range(left, right + 1):
			current = seq[i]
			if current == base:
				seq[i] = seq[gt_base]
				seq[gt_base] = current
				gt_base += 1
			elif current < base:
				seq[i] = seq[gt_base]
				seq[gt_base] = seq[eq_base]
				seq[eq_base] = current
				eq_base += 1
				gt_base += 1
		# если n-й элемент слева от опорного - меняем правую границу
		if n < eq_base:
			right = eq_base - 1
		# если справа - левую
		elif n >= gt_base:
			left = gt_base
		# если n между eq_base и gt_base, то n - й элемент найден
		else:
			return

nums = [int (i) for i in input().split()]

nth_rearrange(nums, 0, len(nums), len(nums) - 1)
# nums[len(nums) -1] == максимальный элемент nums
nth_rearrange(nums, 0, len(nums) - 1, len(nums) - 2)
# nums[len(nums) - 2] == максимум из nums[:-1]
# nums[len(nums) - 3] <= максимум из nums[:-1]
nth_rearrange(nums, 0, len(nums) - 3, 2)
# nums[0] и nums[1] - два минимальных элемента из nums
if nums[-1] * nums[-2] * nums[-3] > nums[-1] * nums[0] * nums[1]:
	print(nums[-1], nums[-2], nums[-3])
else:
	print(nums[-1], nums[0], nums[1])

