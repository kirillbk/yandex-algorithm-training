# A. Объединение последовательностей

x = int(input())

i = j = 1
k = 0
answer = 0
while k < x:
    a = i**2
    b = j**3

    if a < b:
        answer = a
        i += 1
    elif b < a:
        answer = b
        j += 1
    else:
        answer = a
        i += 1
        j += 1
    k += 1

print(answer)
