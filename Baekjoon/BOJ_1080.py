#행렬 실버1
#https://www.acmicpc.net/problem/1080

# M, M = map(int,input().split())
# A = [ ([0]*M) for _ in range(N) ]
# B = [ ([0]*M) for _ in range(N) ]
# # A[0][0], A[1][0], A[2][0]
# # A[1][0], A[1][1], A[1][2]
# # A[2][0], A[2][1], A[2][2]

# A = input()

# for num in range(N):
#     A[num]

N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append([0] * M)
    B.append([0] * M)

for n in range(N):
    num = list(map(int, input().split()))
    for m in range(M):
        A[m][n] = num[m]

for n in range(N):
    num = list(map(int, input().split()))
    for m in range(M):
        B[m][n] = num[m]

print(A)
print(B)