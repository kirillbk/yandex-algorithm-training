# A. Возрастает ли список?
# Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).

# Выведите YES, если массив монотонно возрастает и NO в противном случае.

def	is_ascending(a):
	for i in range(len(a) - 1):
		if a[i] >= a[i + 1]:
			return False
	return True

a = input().split()
if is_ascending(a):
	print("YES")
else:
	print("NO")