# G. Наибольшее произведение двух чисел
# Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально. Выведите эти числа в порядке неубывания.

# Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

# Решение должно иметь сложность O(n), где n - размер списка.

nums = [int (i) for i in input().split()]

max1 = max(nums[0], nums[1])
max2 = min(nums[0], nums[1])
min1 = max2
min2 = max1
for i in range(2, len(nums)):
	if nums[i] > max1:
		max2 = max1
		max1 = nums[i]
	elif nums[i] > max2:
		max2 = nums[i]
	elif nums[i] < min1:
		min2 = min1
		min1 = nums[i]
	elif nums[i] < min2:
		min2 = nums[i]

if max1 * max2 > min1 * min2:
	print(max2, max1)
else:
	print(min1, min2)
