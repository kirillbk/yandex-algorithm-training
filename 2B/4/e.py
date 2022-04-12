n = int(input())
themes = dict()
messages = dict()
for i in range(1, n + 1):
	number = int(input())
	if number == 0:
		theme = input()
		themes[theme] = 0
	else:
		theme = messages[number]
	themes[theme] += 1
	messages[i] = theme
	input()

max_rating = 0
for theme, rating in themes.items():
	if rating > max_rating:
		max_rating = rating
		answer = theme
print(answer)
