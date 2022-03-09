# B. Определить вид последовательности
# По последовательности чисел во входных данных определите ее вид:
# CONSTANT – последовательность состоит из одинаковых значений
# ASCENDING – последовательность является строго возрастающей
# WEAKLY ASCENDING – последовательность является нестрого возрастающей
# DESCENDING – последовательность является строго убывающей
# WEAKLY DESCENDING – последовательность является нестрого убывающей
# RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

# Формат ввода
# По одному на строке поступают числа последовательности ai, |ai| ≤ 109.
# Признаком окончания последовательности является число -2×10^9. Оно в последовательность не входит.

# Формат вывода
# В единственной строке выведите тип последовательности.


seq = []
while True:
	a = int(input())
	# окончание последовтельности
	if a == -2 * 10**9:
		break
	seq.append(a)

eq, lt, gt = False, False, False
for i in range(len(seq) - 1):
	if seq[i] == seq[i + 1]:
		eq = True
	elif seq[i] < seq[i + 1]:
		lt = True
	else:
		gt = True

if lt and gt:
	print('RANDOM')
elif eq:
	if not lt and not gt:
		print('CONSTANT')
	elif lt and not gt:
		print('WEAKLY ASCENDING')
	elif gt and not lt:
		print('WEAKLY DESCENDING')
elif lt:
	print('ASCENDING')
elif gt:
	print('DESCENDING')
