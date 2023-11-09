# E. Поразрядная сортировка

def radix_sort(array: list[str]):
    print("Initial array:")
    print(*array, sep=', ')

    length = len(array[0])

    for i in range(length):
        buckets = [[] for _ in range(10)]
        for s in array:
            idx = int(s[length - i - 1])
            buckets[idx].append(s)

        array = [item for bucket in buckets for item in bucket]

        print("**********")
        print(f"Phase {i + 1}")
        for j in range(len(buckets)):
            print(f"Bucket {j}: ", end='' )
            if buckets[j]:
                print(*buckets[j], sep=', ')
            else:
                print("empty")

    print("**********")
    print("Sorted array:")
    print(*array, sep=', ')

    return array


n = int(input())
s = [input() for _ in range(n)]
radix_sort(s)
