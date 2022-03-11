n = int(input())
folders = list(map(int, input().split()))

print(sum(folders) - max(folders))
