for case in range(1, 1 + int(input())):
    a, b = map(int,input().split())
    print(f'#{case} {a//b} {a%b}')