# 1213. [S/W 문제해결 기본] 3일차 - String D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE&problemTitle=1213&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
for _ in range(1, 11):
    case = int(input())
    index = input()
    words = input()
    words = words.replace(index, '!')
    print(f'#{case} {words.count("!")}')
