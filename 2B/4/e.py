n = int(input())
themes = dict()
messages = dict()
for i in range(n):
	number = int(input())
	if number == 0:
		theme = input()
		themes[theme] = 0
	else:
		theme = messages[number]
	themes[theme] += 1
	messages[i + 1] = theme
	input()

best_rating = 0
for theme, rating in themes.items():
	if rating > best_rating:
		best_rating = rating
		answer = theme
print(answer)
