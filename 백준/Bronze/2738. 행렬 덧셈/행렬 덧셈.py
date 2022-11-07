M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
B = [list(map(int, input().split())) for _ in range(M)]
C = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        print(A[i][j] + B[i][j], end=' ')
    print()
