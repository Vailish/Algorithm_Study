N = int(input())
for num in range(N, 0, -1):  # 오름차순이기 때문에 거꾸로
    if N % num == 0:
        print(int(N/num), end=' ')