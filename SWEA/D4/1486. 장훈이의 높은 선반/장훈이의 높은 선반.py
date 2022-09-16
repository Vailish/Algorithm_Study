def solution(N, B, hights):  # N = 점원 수, B = 탑의 높이, hights = 점원들의 키 리스트
    # 부분집합
    lst = []
    temp = []
    for i in range(1 << N):  # 1<<n : 부분 집합의 개수
        for j in range(N):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번 비트가 1인경우
                temp.append(hights[j])
        lst.append(sum(temp))
        temp = []
    lst.sort()

    index = 0
    for value in lst:
        if value - B >= 0:
            return value - B
    return -1


for case in range(1, 1 + int(input())):
    N, B = map(int, input().split())
    hights = list(map(int, input().split()))
    print(f'#{case} {solution(N, B, hights)}')
