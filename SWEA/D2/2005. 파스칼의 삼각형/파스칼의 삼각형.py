T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1

    for i in range(1, N):
        arr[i][0] = 1
        for j in range(1, N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{case}')
    for i in range(N):
        for j in range(N):
            if i >= j:
                print(arr[i][j], end=' ')
        print()