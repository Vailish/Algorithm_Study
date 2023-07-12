def solution():
    N = int(input())
    men = []
    for _ in range(N):
        men.append(tuple(map(int, input().split())))

    # 덩치 비교하기
    result = []
    for num in range(len(men)):
        tmp = [num, 0]
        for man in men:
            if men[num][0] < man[0] and men[num][1] < man[1]:
                tmp[1] += 1
        tmp[1] += 1
        result.append(tmp)

    # 출력하기
    for i in range(N):
        print(result[i][1], end=" ")


solution()
