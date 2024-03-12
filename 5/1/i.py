# I. Расписание

from calendar import day_name, month_name, isleap


n = int(input())
year = int(input())
holidays = []
for _ in range(n):
    day, month = input().split()
    day = int(day)
    holidays.append((day, month))
day_of_week = input()

m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if isleap(year):
    m_days[2] += 1
mohth_n = {month_name[i]: i for i in range(1, len(month_name))}
day_n = {day_name[i]: i for i in range(len(day_name))}

offset = day_n[day_of_week]
weeks, rem = divmod(offset + sum(m_days), 7)
# количество рабочих дней для каждого дня недели (0 - 6) в году
days = [weeks] * 7
for d in range(0, offset):
    days[d] -= 1
for d in range(0, rem):
    days[d] += 1

for day, month in holidays:
    month = mohth_n[month]
    d = offset + sum(m_days[m] for m in range(month)) + (day - 1)
    days[d % 7] -= 1

# день недели с максимальным/минимальным количеством рабочих дней
best = max((d for d in range(7)), key=lambda x: days[x])
worst = min((d for d in range(7)), key=lambda x: days[x])

print(day_name[best], day_name[worst])
