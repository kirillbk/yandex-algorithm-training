# 4. Контрольная работа

def get_table(place: int):
	table = place // 2
	side = 2
	if place % 2:
		table +=1
		side = 1
	return table, side

def solution(n: int, k: int, table: int, side: int) -> int:
	# p_place - номер пети относительно левого места на первой парте
	p_place = table * 2
	if side == 1:
		p_place -= 1
	# var - вариант, который пишет Петя
	variant = p_place % k
	if variant == 0:
		variant = k

	front = p_place - k
	back = p_place + k

	if k % 2:
		if front > 0:
			return get_table(front)
		elif back <= n:
			return get_table(back)
	elif k % 2 == 0:
		if back <= n:
			return get_table(back)
		elif front > 0:
			return get_table(front)
	return -1,


n = int(input())
k = int(input())
table = int(input())
side = int(input())
print(*solution(n, k, table, side))
