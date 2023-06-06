def solution():
    N = int(input())
    for i in range(N//5, -1, -1):
        for j in range(N//3 + 1):
            if 5 * i + 3 * j == N:
                return i+j
    return -1


print(solution())
