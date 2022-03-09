# C. Второй максимум
# Выведите второй по величине элемент в построенном дереве. Гарантируется, что такой найдется.

# Формат ввода
# Дана последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит.

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

def get_tree_second_max(tree):
	prev_value = None
	while tree[RIGHT]:
		prev_value = tree[VALUE]
		tree = tree[RIGHT]
	if tree[LEFT] == None:
		return prev_value
	tree = tree[LEFT]
	while tree[RIGHT]:
		tree = tree[RIGHT]
	return tree[VALUE]

tree = [None, None, None]
for n in  map(int, input().split()):
	if n != 0:
		insert_tree(tree, n)

print(get_tree_second_max(tree))
