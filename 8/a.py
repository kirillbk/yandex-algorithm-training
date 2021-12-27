# A. Высота дерева
# Реализуйте бинарное дерево поиска для целых чисел. Программа получает на вход последовательность целых чисел и строит из них дерево. Элементы в деревья добавляются в соответствии с результатом поиска их места. Если элемент уже существует в дереве, добавлять его не надо. Балансировка дерева не производится.

# Формат ввода
# На вход программа получает последовательность натуральных чисел. Последовательность завершается числом 0, которое означает конец ввода, и добавлять его в дерево не надо.

# Формат вывода
# Выведите единственное число – высоту получившегося дерева.

def insert_tree(tree, value):
	if tree[0]:
		if n < tree[0]:
			if tree[1] == None:
				tree[1] = [value, None, None]
			else:
				insert_tree(tree[1], value)
		elif n > tree[0]:
			if tree[2] == None:
				tree[2] = [value, None, None]
			else:
				insert_tree(tree[2], value)
	else:
		tree[0] = value

def get_height(tree):
	if tree == None:
		return 0
	left = get_height(tree[1])
	right = get_height(tree[2])
	return max(left, right) + 1

root = [None, None, None]
for n in map(int, input().split()):
	if n != 0:
		insert_tree(root, n)

print(get_height(root))
