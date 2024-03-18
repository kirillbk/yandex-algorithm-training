# C. Петя, Маша и верёвочки

n = int(input())
ropes = list(map(int, input().split()))

longest = ropes[0]
total = ropes[0]
for i in range(1, n):
    if ropes[i] > longest:
        longest = ropes[i]
    total += ropes[i]

if total - longest >= longest:
    print(total)
else:
    print(longest - (total - longest))
