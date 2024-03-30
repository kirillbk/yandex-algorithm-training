# H. Выборы

def find_party(parties: list[tuple[int, int]], n: int) -> tuple[int, int, int]:
    max_votes = max((v for v, _ in parties))

    # prefix[x] - количество голосов, большее чем x
    prefix = [0] * (max_votes + 2)
    for v, _, in parties:
        prefix[v] += 1
    add = prefix[max_votes]
    for i in range(max_votes - 1, 0, -1):
        total = prefix[i] + prefix[i + 1] + add
        add += prefix[i]
        prefix[i] =  total
    prefix[0] = prefix[1]

    price = float('inf')
    idx = -1
    add_votes = 0
    for i in range(n):
        party = parties[i]
        if party[1] == -1:
            continue

        l = 0
        r = max_votes + 1
        while r - l > 1:
            x = (l + r) // 2
            # количество голосов >= x
            votes = prefix[x]
            # убрать из этого количества голоса проверяемой партии
            if party[0] >= x:
                votes -= party[0] - x + 1
            if votes > x - party[0]:
                l = x
            else:
                r = x

        need_votes = r - party[0]
        party_price = need_votes + party[1]
        if party_price < price:
            price = party_price
            idx = i
            add_votes = need_votes

    return price, idx, add_votes


n = int(input())
parties = []
for _ in range(n):
    v, p = map(int, input().split())
    parties.append([v, p])

votes_before = sum((v for v, _ in parties))
price, idx, votes = find_party(parties, n)
parties[idx][0] += votes

# количество голосов у любой партии должно быть меньше, чем у победившей
for i in range(n):
    if i == idx:
        continue
    party = parties[i]
    if party[0] >= parties[idx][0]:
        votes -= party[0] - parties[idx][0] + 1
        party[0] = parties[idx][0] - 1

# оставшиеся голоса можно забрать у любой партии
for i in range(n):
    if i == idx:
        continue
    party = parties[i]
    if party[0] > votes:
        party[0] -= votes
        votes = 0
        break
    else:
        votes -= party[0]
        party[0] = 0

votes_after = sum((v for v, _ in parties))
assert votes_before == votes_after

print(price)
print(idx + 1)
print(*(v for v, _ in parties))


