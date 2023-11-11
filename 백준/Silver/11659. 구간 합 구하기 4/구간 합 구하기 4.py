import sys
input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    lst = [0]
    tmp_num = 0
    for i in range(n):
        tmp_num += tmp[i]
        lst.append(tmp_num)

    for _ in range(m):
        i, j = map(int, input().split())
        answer = lst[j] - lst[i-1]
        print(answer)


solution()
