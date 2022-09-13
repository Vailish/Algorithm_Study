for case in range(1, 1 + int(input())):
    n = 1
    lst = []
    k = int(input())
    while True:
        for chr in str(k * n):
            lst.append(int(chr))
        if sorted(list(set(lst))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(f'#{case} {k * n}')
            break
        n += 1
