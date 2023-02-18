class Heap:

	def __init__(self) -> None:
		self._data = list()

	def insert(self, x):
		self._data.append(x)
		i = len(self._data) - 1
		while i > 0 and self._data[i] > self._data[(i - 1) // 2]:
			self._data[i], self._data[(i - 1) // 2] = self._data[(i - 1) // 2], self._data[i]
			i = (i - 1) // 2

	def extract(self):
		top = self._data[0]
		self._data[0] = self._data[-1]
		self._data.pop()
		i = 0
		while i * 2 + 1 < len(self._data):
			l = i * 2 + 1
			r = i * 2 + 2
			child = l
			if r < len(self._data) and self._data[r] > self._data[l]:
				child = r
			if self._data[i] > self._data[child]:
				break
			self._data[i], self._data[child] = self._data[child], self._data[i]
			i = child
		return top


n = int(input())
heap = Heap()
result = list()
for _ in range(n):
	cmd = input().split()
	if cmd[0] == '0':
		heap.insert(int(cmd[1]))
	else:
		result.append(heap.extract())

print(*result, sep='\n')
