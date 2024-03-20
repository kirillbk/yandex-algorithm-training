# B. Анаграмма?

from collections import Counter


cntr1 = Counter(input())
cntr2 = Counter(input())
if cntr1 == cntr2:
    print('YES')
else:
    print('NO')
