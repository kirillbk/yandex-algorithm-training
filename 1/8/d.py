# D. Обход
# Выведите все элементы полученного дерева в порядке возрастания.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит. По данной последовательности требуется построить дерево.

# Формат вывода
# Выведите ответ на задачу.

VALUE = 0
LEFT = 1
RIGHT = 2

def insert_tree(tree, value):
	if tree[VALUE]:
		if value < tree[VALUE]:
			if tree[LEFT]:
				insert_tree(tree[LEFT], value)
			else:
				tree[LEFT] = [value, None, None]
		elif value > tree[VALUE]:
			if tree[RIGHT]:
				insert_tree(tree[RIGHT], value)
			else:
				tree[RIGHT] = [value, None, None]
	else:
		tree[VALUE] = value

def print_tree_asc(tree):
	if tree == None:
		return
	print_tree_asc(tree[LEFT])
	print(tree[VALUE])
	print_tree_asc(tree[RIGHT])

tree = [None, None, None]
for n in map(int, input().split()):
	if n != 0:
		insert_tree(tree, n)
print_tree_asc(tree)
