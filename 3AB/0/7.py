# 7. SNTP


def get_time(time: str) -> int:
	h, m, s = map(int, time.split(':'))
	return s + m * 60 + h * 3600


a = get_time(input())
b = get_time(input())
c = get_time(input())

if c < a:
	c += 24*3600
offset = c - a
offset = int(offset / 2) + offset % 2
h, s = divmod(b + offset, 3600)
m, s = divmod(s, 60)
h %= 24
print(f'{h:02}:{m:02}:{s:02}')
