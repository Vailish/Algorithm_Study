def solution(n):
    length = 10**int(18/3) + 1  # N 조건식
    for i in range(1, length):
        if i**3 == n:
            return f'#{case} {i}'
    return f'#{case} -1'


for case in range(1, 1 + int(input())):
    print(solution(int(input())))
