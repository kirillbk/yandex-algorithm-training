# D. Реклама
# Фирма NNN решила транслировать свой рекламный ролик в супермаркете XXX. Однако денег, запланированных на рекламную кампанию, хватило лишь на две трансляции ролика в течение одного рабочего дня.
# Фирма NNN собрала информацию о времени прихода и времени ухода каждого покупателя в некоторый день. Менеджер по рекламе предположил, что и на следующий день покупатели будут приходить и уходить ровно в те же моменты времени.
# Помогите ему определить моменты времени, когда нужно включить трансляцию рекламных роликов, чтобы как можно большее количество покупателей прослушало ролик целиком от начала до конца хотя бы один раз. Ролик длится ровно 5 единиц времен. Трансляции роликов не должны пересекаться, то есть начало второй трансляции должно быть хотя бы на 5 единиц времени позже, чем начало первой.
# Если трансляция ролика включается, например, в момент времени 10, то покупатели, пришедшие в супермаркет в момент времени 10 (или раньше) и уходящие из супермаркета в момент 15 (или позднее) успеют его прослушать целиком, а, например, покупатель, пришедший в момент времени 11, равно как и покупатель, уходящий в момент 14 - не успеют.
# Если покупатель успевает услышать только конец первой трансляции ролика (не сначала) и начало второй трансляции (не до конца), то считается, что он не услышал объявления. Если покупатель успевает услышать обе трансляции ролика, то при подсчете числа людей, прослушавших ролик, он все равно учитывается всего один раз (фирме важно именно количество различных людей, услышавших ролик).

# Формат ввода
# В первой строке входного файла вводится число N - количество покупателей (1 ≤ N ≤ 2000). В следующих N строках записано по паре натуральных чисел - время прихода и время ухода каждого из них. Все значения времени - натуральные числа, не превышающие 109. Время ухода человека из супермаркета всегда строго больше времени его прихода в супермаркет.

# Формат вывода
# Выведите через пробел три числа: количество покупателей, которые прослушают ролик целиком от начала до конца хотя бы один раз, и моменты времени, когда должна начинаться трансляция ролика. Моменты времени должны быть выведены в возрастающем порядке и должны быть натуральными числами, не превышающими 2·10^9. Если вариантов ответа несколько, выведите любой из них.

# Решение из разбора (сложно!!!)

IN = -1
OUT = 1

n = int(input())
events = []
for i in range(n):
	enter, leave = map(int, input().split())
	# покупатели, которые провели в магазине меньше 5 минут нас не интересуют
	# рассматриваем только моменты прихода покупателей и за 5 минут до ухода
	if leave - enter >= 5:
		events.append((enter, IN, i))
		events.append((leave - 5, OUT, i))

events.sort()
# все покупатели провели в магазине меньше 5 минут
if len(events) == 0:
	print(0, 0, 21)
# есть только один покупатель, который провёл в магазине больше 5 минут
elif len(events) == 2:
	print(1, events[0][0], events[0][0] + 21)
else:
	# количество покупателей, которое прослушало хотя бы одну рекламу
	best_ans = 0
	# моменты трансляции первой и второй рекламы
	first_ans, second_ans = 0, 0
	# множество людей прослушавших первую рекламу
	first_ad = set()
	for i in range(len(events)):
		event1 = events[i]
		# включаем первый рекламный ролик, если пришёл покупатель
		if event1[1] == IN:
			first_ad.add(event1[2])
			# проверка если все покупатели прослушали 1-ю рекламу
			if len(first_ad) > best_ans:
				best_ans = len(first_ad)
				first_ans = event1[0]
				second_ans = event1[0] + 5
		# ищем момент включения второго ролика
		second_ad_cnt = 0
		for j in range(i + 1, len(events)):
			event2 = events[j]
			if event2[1] == IN and event2[2] not in first_ad:
				second_ad_cnt += 1
			# разница между показом 1-го и второго ролика больше 5 минут
			# больше покупателей послушали 1-й и 2-й ролик, обновляем ответ
			if event2[0] - 5 >= event1[0] and len(first_ad) + second_ad_cnt > best_ans:
				best_ans = len(first_ad) + second_ad_cnt
				first_ans = event1[0]
				second_ans = event2[0]
			if event2[1] == OUT and event2[2] not in first_ad:
				second_ad_cnt -= 1
		if event1[1] == OUT:
			first_ad.remove(event1[2])

	print(best_ans, first_ans, second_ans)
