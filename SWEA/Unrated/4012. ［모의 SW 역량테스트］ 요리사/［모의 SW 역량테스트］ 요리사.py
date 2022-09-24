from itertools import combinations


def solution(n):
    # n개의 숫자에서 n/2개를 뽑고 (부분집합)
    result = []
    numbers = list(i for i in range(n))
    for numbers_a in combinations(numbers, n//2):
        numbers_b = list(set(numbers) - set(numbers_a))
        numbers_a = list(numbers_a)
        # 나온 숫자들로 두 개를 뽑아 순열을 돌고
        tmp_a = 0
        for i, j in combinations(numbers_a, 2):
            # 그 값들을 배열에 넣어서 값들을 전부 더한다.
            tmp_a += S[i][j] + S[j][i]
        # 반대(B)의 요리도 같은 방식으로 진행한다.
        tmp_b = 0
        for x, y in combinations(numbers_b, 2):
            tmp_b += S[x][y] + S[y][x]
        # A와 B의 차를 구한다
        result.append(abs(tmp_a - tmp_b))
    return min(result)


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 식재료 수
    S = [list(map(int, input().split())) for _ in range(N)]  # S
    print(f'#{case} {solution(N)}')