for case in range(1, 1 + int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f"#{case}", end=' ')
    for num in numbers:
        print(num, end=' ')
    print()
