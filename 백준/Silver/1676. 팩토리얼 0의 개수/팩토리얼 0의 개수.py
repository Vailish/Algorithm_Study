def solution():
    N = int(input())
    value = 1
    for i in range(1, N+1):
        value *= i
    num = str(value)
    cnt = 0
    for j in range(len(num) -1, -1, -1):
        if num[j] == "0":
            cnt += 1
        else:
            return cnt
    return 0


print(solution())
