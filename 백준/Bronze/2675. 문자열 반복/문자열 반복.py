for _ in range(int(input())):
    num, chr = input().split()
    for c in chr:
        print(c*int(num), end='')
    print()