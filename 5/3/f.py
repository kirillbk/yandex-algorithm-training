# F. Замена слов

dictionary = set(input().split())
text = input().split()

answer = []
for word in text:
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in dictionary:
            answer.append(prefix)
            break
    else:
        answer.append(word)

print(*answer)
