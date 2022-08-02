#출처 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=1986&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

#1986
#지그재그 숫자
#D2

T = int(input())  # 총 횟수
list = []
for _ in range(0, T) :
    list.append(input()) # 횟수별 입력값
sum = 0
t = 1
for n in list: #횟수별 계산
    if int(n) % 2 == 1:
        sum += int(n)
    else:
        sum -= int(n)
    print(f'#{t} {sum}')  #한 횟수당 출력 
    t += 1