# E. Вывод листьев
# Для полученного дерева выведите список всех листьев (вершин, не имеющих потомков) в порядке возрастания.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит.

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

def print_tree_leafs(tree):
	if tree == None:
		return
	print_tree_leafs(tree[LEFT])
	if tree[LEFT] == None and tree[RIGHT] == None:
		print(tree[VALUE])
	print_tree_leafs(tree[RIGHT])

tree = [None, None, None]
for n in map(int, input().split()):
	if n != 0:
		insert_tree(tree, n)

print_tree_leafs(tree)
