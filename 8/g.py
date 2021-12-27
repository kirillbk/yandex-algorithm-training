# G. Вывод веток
# Для полученного дерева выведите список всех вершин, имеющих только одного ребёнка, в порядке возрастания.

# Формат ввода
# Вводится последовательность целых чисел,оканчивающаяся нулем. Построить по ней дерево.

# Формат вывода
# Выведите список требуемых вершин.

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

def print_tree_single_child(tree):
	if tree == None:
		return
	print_tree_single_child(tree[LEFT])
	if tree[LEFT] and tree[RIGHT] == None or tree[LEFT] == None and tree[RIGHT]:
		print(tree[VALUE])
	print_tree_single_child(tree[RIGHT])

tree = [None, None, None]
for n in map(int, input().split()):
	if n != 0:
		insert_tree(tree, n)

print_tree_single_child(tree)
