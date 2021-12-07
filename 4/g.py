# G. Банковские счета
# Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:
# Пополнение счета клиента.
# Снятие денег со счета.
# Запрос остатка средств на счете.
# Перевод денег между счетами клиентов.
# Начисление процентов всем клиентам.
# Вам необходимо реализовать такую систему.
# Клиенты банка идентифицируются именами (уникальная строка, не содержащая пробелов).
# Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия или перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом. Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.

# Формат ввода
# Входной файл содержит последовательность операций. Возможны следующие операции:
# DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет счета, то счет создается.
# WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет счета, то счет создается.
# BALANCE name - узнать остаток средств на счету клиента name.
# TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у какого-либо клиента нет счета, то ему создается счет.
# INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета. Проценты начисляются только клиентам с положительным остатком на счету, если у клиента остаток отрицательный, то его счет не меняется. После начисления процентов сумма на счету остается целой, то есть начисляется только целое число денежных единиц. Дробная часть начисленных процентов отбрасывается.

# Формат вывода
# Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента. Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите ERROR.

from collections import defaultdict
from sys import stdin

class Bank:
	def __init__(self):
		self.db = defaultdict(int)

	def operation(self, query):
		if query[0] == 'DEPOSIT':
			self.deposit(query[1], int(query[2]))
		elif query[0] == 'WITHDRAW':
			self.withdraw(query[1], int(query[2]))
		elif query[0] == 'BALANCE':
			self.balance(query[1])
		elif query[0] == 'TRANSFER':
			self.transfer(query[1], query[2], int(query[3]))
		elif query[0] == 'INCOME':
			self.income(int(query[1]))

	def deposit(self, name, sum):
		self.db[name] += sum

	def withdraw(self, name, sum):
		self.db[name] -= sum
	
	def balance(self, name):
		if name not in self.db:
			print("ERROR")
		else:
			print(self.db[name])
	
	def transfer(self, name1, name2, sum):
		self.db[name1] -= sum
		self.db[name2] += sum
	
	def income(self, p):
		for name in self.db:
			balance = self.db[name]
			if (balance > 0):
				self.db[name] +=  int(balance * p / 100)

operations = []
for line in stdin:
	operations.append(line.split())

bank = Bank()
for query in operations:
	bank.operation(query)
