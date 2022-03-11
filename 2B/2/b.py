HOUSE = 1
STORE = 2

street = list(map(int, input().split()))

distance_to_left_store = [0] * len(street)
#find distance from each house to left store
shop_idx = - 2 * len(street)
for i in range(len(street)):
	if street[i] == STORE:
		shop_idx = i
	elif street[i] == HOUSE:
		distance_to_left_store[i] = i - shop_idx
#find minimum distance from each house to store and maximum distance to store 
answer = 0
shop_idx = 2 * len(street)
for i in range(len(distance_to_left_store) - 1, -1, -1):
	if street[i] == STORE:
		shop_idx = i
	elif street[i] == HOUSE:
		distance = min(distance_to_left_store[i], shop_idx - i)
		answer = max(distance, answer)

print(answer)
