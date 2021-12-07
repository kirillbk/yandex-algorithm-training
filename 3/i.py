# I. Полиглоты
# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

# Формат ввода
# Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник. Длина названий языков не превышает 1000 символов, количество различных языков не более 1000. 1 ≤ N ≤ 1000, 1 ≤ Mi ≤ 500.

# Формат вывода
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.

n = int(input())
students = [[] for _ in range(n)]
for i in range(n):
	m = int(input())
	for _ in range(m):
		students[i].append(input())

everyone_knows = set(students[0])
anyone_knows = set(students[0])
for i in range(1, n):
	everyone_knows = everyone_knows.intersection(students[i])
	anyone_knows.update(students[i])

print(len(everyone_knows))
print('\n'.join(everyone_knows))
print(len(anyone_knows))
print('\n'.join(anyone_knows))
