from sys import stdin

NO = 0
PARTY = 1
VOTES = 2
SEATS = 3
REMAINDER = 4

elections = list()
total_votes = 0
i = 0
for line in stdin:
	party, votes = line.rsplit(' ', 1)
	votes = int(votes)
	elections.append([i, party, votes])
	total_votes += votes
	i += 1

first_quotient = total_votes / 450
free_seats = 450
for party in elections:
	party.append(int(party[VOTES] // first_quotient))
	party.append(party[VOTES] % first_quotient)
	free_seats -= party[SEATS]
elections.sort(key=lambda x: x[REMAINDER], reverse=True)
for i in range(int(free_seats)):
	elections[i][SEATS] += 1
elections.sort(key=lambda x: x[NO])

for party in elections:
	print(party[PARTY], party[SEATS])
