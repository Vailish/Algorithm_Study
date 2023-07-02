def solution():
    lst = []
    for _ in range(int(input())):
        lst.append(tuple(map(int, input().split())))
    for v1, v2 in sorted(lst, key=lambda x: (x[0], x[1])):
        print(v1, v2)


solution()
