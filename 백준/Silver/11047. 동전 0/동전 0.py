N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
result = 0

for i in range(N - 1, -1, -1):
    result += K//coins[i]
    K %= coins[i]
    if K == 0:
        break

print(result)
