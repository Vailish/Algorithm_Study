while True:
    A, B = map(int,input().split())
    if A == 0 and B == 0: #출력값 개수보면 종료시점 알 수 있음
        break
    else:
        print(A+B)