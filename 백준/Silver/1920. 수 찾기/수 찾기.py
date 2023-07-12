N = int(input())
n = set(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in range(M):
    if m[i] in n:
        print(1)
    else:
        print(0)
