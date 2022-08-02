import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for order in range(1, T + 1):
    N, K = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    array_r, array_c = [], []  # 가로와 세로 개수를 따로 구하기 위해 리스트 2개를 선언
    for i in range(N):  # 값들을 그대로 새로운 리스트에 복사해준다.
        temp1 = []
        temp2 = []
        for j in range(N):
            temp1.append(array[i][j])
            temp2.append(array[i][j])
        array_r.append(temp1)
        array_c.append(temp2)

    result = 0  # 총 결과를 출력할 변수

    # 세로 계산
    for i in range(N):
        for j in range(N):
            count = 0  # 흰색블럭 개수를 셀 변수
            for h in range(i, N):  # 어떠한 인덱스에서 밑으로 쭉 검사한다.(세로 한줄을 검사)
                if array_c[h][j] == 0:  # 만약 해당 인덱스의 값이 검은색 블럭이면
                    break  # 바로 다음 열 검사를 위해 이동
                count += 1  # 만약 흰색 블럭이라면 개수 +1
                array_c[h][j] = 0  # 그 후 조사한 블럭을 0으로 처리
            if count == K:  # 만약 다돌고 난 후 그 개수가 k개 라면
                result += 1  # 결과에 +1

    # 가로 계산
    for i in range(N):
        for j in range(N):
            count = 0  # 흰색블럭 개수를 셀 변수
            for h in range(j, N):  # 어떠한 인덱스에서 옆으로 쭉 검사한다.(가로 한줄을 검사)
                if array_r[i][h] == 0:  # 만약 해당 인덱스의 값이 검은색 블럭이면
                    break  # 탈출 후 다음 열로 이동
                count += 1  # 만약 흰색 블럭이라면 개수 +1
                array_r[i][h] = 0  # 그후 조사한 블럭을 검은색 블럭으로 처리
            if count == K:  # 다 돌고 난후 흰색 블럭 개수가 K개 라면
                result += 1  # 결과에 +1

    print(f'#{order} {result}')