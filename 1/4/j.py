# J. Дополнительная проверка на списывание
# Преподаватель курса ОиМП заказал у одного известного психолога полное психологическое обследование всех студентов,
# поступивших на ФНК с целью выяснить их склонность к списыванию еще до начала занятий и отчислить их за списывание еще до того как они приступят к занятиям и смогут позорить ФНК своими преступлениями.
# Психолог, привлеченный для проведения обследования, известен своим инновационным методом, позволяющим понять склонность к списыванию студента по наиболее часто используемому им в программах идентификатору.
# Помогите известному психологу определить, какие из студентов потенциально являются преступниками. Напишите программу, которая по приведенной программе выяснит наиболее часто используемый в ней идентификатор.
# Поскольку разные студенты на тестировании пишут программы на разных языках программирования, ваша программа должна уметь работать с произвольным языком. Поскольку в разных языках используются различные ключевые слова, то список ключевых слов в анализируемом языке предоставляется на вход программе.
# Все последовательности из латинских букв, цифр и знаков подчеркивания, которые не являются ключевыми словами и содержат хотя бы один символ, не являющийся цифрой, могут быть идентификаторами.
# При этом в некоторых языках идентификаторы могут начинаться с цифры, а в некоторых - нет. Если идентификатор не может начинаться с цифры, то последовательность, начинающаяся с цифры, идентификатором не является. Кроме этого, задано, является ли язык чувствительным к регистру символов, используемых в идентификаторах и ключевых словах.

# Формат ввода
# В первой строке вводятся число n - количество ключевых слов в языке (0 <= n <= 50) и два слова C и D, каждое из которых равно либо "yes", либо "no". Слово C равно "yes", если идентификаторы и ключевые слова в языке чувствительны к регистру символов, и "no", если нет. Слово D равно "yes", если идентификаторы в языке могут начинаться с цифры, и "no", если нет.
# Следующие n строк содержат по одному слову, состоящему из букв латинского алфавита и символов подчеркивания - ключевые слова. Все ключевые слова непусты, различны, при этом, если язык не чувствителен к регистру, то различны и без учета регистра. Длина каждого ключевого слова не превышает 50 символов.
# Далее до конца входных данных идет текст программы. Он содержит только символы с ASCII-кодами от 32 до 126 и переводы строки.
# Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один идентификатор.

# Формат вывода
# Выведите идентификатор, встречающийся в программе максимальное число раз. Если таких идентификаторов несколько, следует вывести тот, который встречается в первый раз раньше. Если язык во входных данных не чувствителен к регистру, то можно выводить идентификатор в любом регистре.

# Решение из разбора

from sys import stdin
from collections import defaultdict

# убрать из строки все символы, неиспользуемые для идентификаторов и разбить на слова
def split_to_words(line):
	buffer = []
	for c in line:
		if c.isalpha() or c.isdigit() or c == '_':
			buffer.append(c)
		else:
			buffer.append(' ')
	return ''.join(buffer).split()


n, c, d = input().split()
n = int(n)
c = c == 'yes'
d = d == 'yes'
# создадим и заполним множество с ключевыми словами
key_words = set()
for _ in range(n):
	word = input()
	if not c:
		word = word.lower()
	key_words.add(word)

# создадим и заполним словарь с идентификаторами и количеством их вхождений
identifiers = defaultdict(int)
for line in stdin:
	words = split_to_words(line)
	for word in words:
		if not c:
			word = word.lower()
		# если слово не может быть идентификатором - continue
		if word in key_words or word.isdigit() or (not d and word[0].isdigit()):
			continue
		identifiers[word] += 1

# найдём первый идентификатор с масимальным количеством вхождений
# начиная с Python 3.6 порядок ключей в словаре соответствует порядку их добавления
common_id = ''
max_qty = 0
for id, qty in identifiers.items():
	if qty > max_qty:
		max_qty = qty
		common_id = id

print(common_id)
