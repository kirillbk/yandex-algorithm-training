# B. Глубина добавляемых элементов
# В бинарное дерево поиска добавляются элементы. Выведите глубину для каждого добавленного элемента в том порядке, как они добавлялись.
# Если элемент уже есть в дереве, то ничего добавлять и выводить не нужно. Глубиной называется расстояние от корня дерева до элемента включительно.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит. По данной последовательности требуется построить дерево.

# Формат вывода
# Выведите ответ на задачу.

VALUE = 0
LEFT = 1
RIGHT = 2

def insert_tree(tree, value, ans):
	if tree[VALUE] == None:
		tree[VALUE] = value
		ans.append(1)
	depth = 1
	while True:
		depth += 1
		if value < tree[VALUE]:
			if tree[LEFT] == None:
				tree[LEFT] = [value, None, None]
				ans.append(depth)
				return
			else:
				tree = tree[LEFT]
		elif value > tree[VALUE]:
			if tree[RIGHT] == None:
				tree[RIGHT] = [value, None, None]
				ans.append(depth)
				return
			else:
				tree = tree[RIGHT]
		else:
			return

ans = []
tree = [None, None, None]
for n in map(int, input().split()):
	if n != 0:
		insert_tree(tree, n, ans)
print(*ans)
