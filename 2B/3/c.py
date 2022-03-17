from collections import Counter

print(*(value for value, freq in Counter(input().split()).items() if freq == 1))
