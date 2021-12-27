# H. АВЛ-сбалансированность
# Дерево называется АВЛ-сбалансированным, если для любой его вершины высота левого и правого поддерева для этой вершины различаются не более чем на 1.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит. Постройте дерево, соответствующее данной последовательности.

# Формат вывода
# Определите, является ли дерево сбалансированным, выведите слово YES или NO.

VALUE = 0
LEFT = 1
RIGHT = 2

def insert_tree(tree, value):
	if tree[VALUE]:
		if value < tree[VALUE]:
			if tree[LEFT]:
				insert_tree(tree[LEFT], n)
			else:
				tree[LEFT] = [value, None, None]
		elif value > tree[VALUE]:
			if tree[RIGHT]:
				insert_tree(tree[RIGHT], n)
			else:
				tree[RIGHT] = [value, None, None]
	else:
		tree[VALUE] = value

def is_tree_avl(tree):
	if tree == None:
		return 0
	left = is_tree_avl(tree[LEFT])
	if left == -1:
		return -1
	right = is_tree_avl(tree[RIGHT])
	if right == -1:
		return -1
	if abs(left - right) > 1:
		return -1
	return max(left, right) + 1

tree = [None, None, None]
for n in map(int, input().split()):
	if n != 0:
		insert_tree(tree, n)

if is_tree_avl(tree) != -1:
	print('YES')
else:
	print('NO')
