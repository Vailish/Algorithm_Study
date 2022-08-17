for case in range(1, int(input())+1):
    N = int(input())

    # 정사각형을 만든 뒤, 0으로 채워 넣는다.
    arr = [[0] * N for _ in range(N)]

    # 1열을 전부 1로 채워 넣는다.
    for i in range(N):
        arr[i][0] = 1

    # 파스칼 규칙에 따라서 값을 채워 넣는다.
    for i in range(1, N):
        for j in range(1, i + 1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # 필요한 부분을 출력한다
    print(f'#{case}')
    for i in range(N):
        for j in range(N):
            if i >= j:
                print(arr[i][j], end=' ')
        print()