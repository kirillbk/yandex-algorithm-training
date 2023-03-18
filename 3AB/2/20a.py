# 20. Машинки

from heapq import heappush, heapreplace


n, k, p = map(int, input().split())
cars = [[0, 0] for _ in range(p)]
for i in range(p):
	cars[i][1] = int(input())

# для каждой машинки определим время(индекс), когда она будет использоваться в следующий раз, отрицательное значение для heapq
cars_next_use = [-p] * (n + 1)
for i in range(p-1, -1, -1):
	car_no = cars[i][1]
	cars[i][0] = cars_next_use[car_no]
	cars_next_use[car_no] = -i

game_cars = set()
# на вершине кучи будет находиться машинка с максимальным временем следующего использования
heap = list()
answer = 0
for next_use, car_no in cars:
	if car_no not in game_cars:
		if len(game_cars) == k:
			take_off_car = heapreplace(heap, (next_use, car_no))[1]
			game_cars.discard(take_off_car)
		else:
			heappush(heap, (next_use, car_no))
		game_cars.add(car_no)
		answer += 1
	else:
		heappush(heap, (next_use, car_no))

print(answer)
