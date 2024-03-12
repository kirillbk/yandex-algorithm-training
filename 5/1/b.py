# B. Футбольный комментатор

g11, g12 = map(int, input().split(':'))
g21, g22 = map(int, input().split(':'))
home = input().strip() == '1'

team1 = g11 + g21
team2 = g12 + g22
goals = 0
if team1 <= team2:
    goals = team2 - team1
    if home and g21 + goals <= g12 or not home and g11 <= g22:
        goals += 1

print(goals)
