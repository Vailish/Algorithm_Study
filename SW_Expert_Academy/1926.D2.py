#출처 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=1926&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#1926
#간단한 369게임
#D2

N = int(input())
answer = ""
for num in range(1, N+1):
    answer += str(num) + " "
answer.replace('3', '-')
answer.replace('6', '-')
answer.replace('9', '-')

print(answer)

#.replace(old, new, count)
#문자열에서 사용가능
#old : 바뀔 녀석
#new : 바꿀 녀석
#count : 횟수

# N = int(input())
# answer = ''
# for num in range(1, N+1):
#     if num > 9:
#         if num[0] == '3' or '6' or '9':
#             num[0] = '-'
#         if num[1] == '3' or '6' or '9':
#             num[1] = '-'
#     else: #num <= 9
#         if str(num) == '3' or '6' or '9':
#             num = '-'
#         answer += num
    
#     print(num, end=" ")

