idx = {1: 2,
       2: 1}


def solution():
    result = []  # 매 열의 교착 수
    for j in range(100):
        cnt = 0  # 종류가 바뀔 때 카운트
        num = 0  # 현재의 숫자(1 또는 2)
        for i in range(100):
            # 처음 값 설정
            if field[i][j] != 0 and num == 0:
                num = field[i][j]
                if num == 2:  # 위 N극(1)이니까 다르면 빼주기
                    cnt -= 1
            # 다른 종류일 때 카운트 해주기
            elif num != 0 and field[i][j] == idx.get(num):
                cnt += 1
                num = field[i][j]
        if num == 1:  # 아래 S극(2)니까 다르면 빼주기
            cnt -= 1
        if cnt >= 1:
            cnt = (cnt + 1)//2
        result.append(cnt)
    return sum(result)


for case in range(1, 11):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case}', solution())
