# E. Два из трех

input()
s1 = set(map(int, input().split()))
input()
s2 = set(map(int, input().split()))
input()
s3 = set(map(int, input().split()))

answer = s1 & s2 | s1 & s3 | s2 & s3

print(*sorted(answer))
