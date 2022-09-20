for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    binary_number = bin(M)[2:]
    if len(binary_number) >= N and '0' not in binary_number[len(binary_number)-N:]:
        print(f'#{case} ON')
    else:
        print(f'#{case} OFF')
