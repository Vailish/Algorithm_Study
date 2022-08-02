# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())
A = []
B = []
result = []
for _ in range(M):
    A.append([0] * N)
    B.append([0] * N)
    result.append([0] * N)

for m in range(M):
    num = list(map(int, input().split()))
    for n in range(N):
        A[m][n] = num[n]

for m in range(M):
    num = list(map(int, input().split()))
    for n in range(N):
        B[m][n] = num[n]

for m in range(M):
    for n in range(N):
        result[m][n] = A[m][n] + B[m][n]

print(result)
#A[0][0] A[0][1] A[0][2]
#A[1][0] A[1][1] A[1][2]
#A[2][0] A[2][1] A[2][2]