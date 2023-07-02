def solution():
    lst = []
    for _ in range(int(input())):
        lst.append(tuple(input().split()))

    lst.sort(key=lambda x: int(x[0]))

    for v1, v2 in lst:
        print(v1, v2)

solution()
