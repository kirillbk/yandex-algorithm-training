# I. Родословная: число потомков
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Для каждого элемента дерева определите число всех его потомков (не считая его самого).

# Формат ввода
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

# Формат вывода
# Выведите список всех элементов в лексикографическом порядке, для каждого элемента выводите количество всех его потомков.

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

def count_descendants(name, tree, descendants):
	if descendants[name] != -1:
		return
	cntr = len(tree[name])
	for child in tree[name]:
		# если для потомка неизвестно количество потомков - посчитаем
		if descendants[child] == -1:
			count_descendants(child, tree, descendants)
		cntr += descendants[child]
	descendants[name] = cntr

n = int(input())
# родитель : список потомков
tree = defaultdict(list)
# элемент дерева : количество потомков
descendants = {}
for _ in range(n - 1):
	child, parent = input().split()
	tree[parent].append(child)
	if child not in descendants:
		descendants[child] = -1
	if parent not in descendants:
		descendants[parent] = -1

for name in sorted(descendants.keys()):
	count_descendants(name, tree, descendants)
	print(name, descendants[name])
