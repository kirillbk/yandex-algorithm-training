# A. Плейлисты

from collections import defaultdict


songs = defaultdict(int)
n = int(input())
for _ in range(n):
    k = int(input())
    for song in input().split():
        songs[song] += 1

answer = [song for song, cntr in songs.items() if cntr == n]
answer.sort()

print(len(answer))
print(*answer)
