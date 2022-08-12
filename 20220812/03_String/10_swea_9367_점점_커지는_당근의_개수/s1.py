# 9367. 점점 커지는 당근의 개수 D1
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AW_nY2m6OLADFARY

T = int(input())
for case in range(1, 1 + T):
    N = int(input())
    C = list(map(int, input().split()))
    number = 1
    result = []

    for i in range(len(C)-1):
        if C[i]+1 == C[i+1]:
            number += 1
        else:
            result.append(number)
            number = 1
    result.append(number)
    max_num = 0
    for num in range(len(result)):
        if max_num < result[num]:
            max_num = result[num]
    print(f'#{case} {max_num}')
