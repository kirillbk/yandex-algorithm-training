# J. Родословная: подсчет уровней
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя. Вам дано генеалогическое древо, определите высоту всех его элементов.

# Формат ввода
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N-1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

# Формат вывода
# Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента необходимо вывести его высоту.

# v 2

from collections import defaultdict

def get_height(name, tree, heights):
	if heights[name] != -1:
		return
	height = 0
	if tree[name]:
		if heights[tree[name]] == -1:
			get_height(tree[name], tree, heights)
		height = heights[tree[name]] + 1
	heights[name] = height

n = int(input())
# потомок : родитель
tree = defaultdict(list)
# элемент дерева : высота
heights = {}
for _ in range(n - 1):
	child, parent = input().split()
	tree[child] = parent
	if parent not in tree:
		tree[parent] = None
	if parent not in heights:
		heights[parent] = -1
	if child not in heights:
		heights[child] = -1

for name in sorted(heights.keys()):
	get_height(name, tree, heights)
	print(name, heights[name])


# v 1

# def get_height(name, tree):
# 	height = 0
# 	while tree[name]:
# 		height += 1
# 		name = tree[name]
# 	return height

# n = int(input())
# tree = {}
# for _ in range(n - 1):
# 	child, parent = input().split()
# 	tree[child] = parent
# 	if parent not in tree:
# 		tree[parent] = None

# for name in sorted(tree.keys()):
# 	print(name, get_height(name, tree))