def solution():
    lst = []
    for _ in range(int(input())):
        lst.append(tuple(map(int, input().split())))
    for a, b in sorted(lst, key=lambda x: (x[1], x[0])):
        print(a, b)


solution()