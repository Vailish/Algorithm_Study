def solution():
    apartment = [[0] * 14 for _ in range(15)]  # 0층도 포함하기 때문
    # 아파트 주민 수 채우기
    # 0층
    for j in range(14):
        apartment[0][j] = j + 1
    # 나머지층
    for i in range(1, 15):
        for j in range(14):
            tmp = 0
            for k in range(j+1):
                tmp += apartment[i-1][k]
            apartment[i][j] = tmp

    for _ in range(int(input())):
        k = int(input())
        n = int(input())
        print(apartment[k][n-1])


solution()
