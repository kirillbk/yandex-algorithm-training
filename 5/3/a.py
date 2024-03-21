# A. Плейлисты


n = int(input())
k = input()
songs = set(input().split())
for _ in range(n - 1):
    k = input()
    songs = songs.intersection(input().split())
answer = sorted(songs)

print(len(answer))
print(*answer)
