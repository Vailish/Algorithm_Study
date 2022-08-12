# 9386. 연속한 1의 개수 D1
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXALDUIq97oDFASI

# 0을 기준으로 나눈 뒤, len을 사용해서 최대값을 구한다.
for case in range(1, int(input())+1):
    N = int(input())
    nums = input().split('0')
    count_max = 0
    for num in nums:
        if count_max < len(num):
            count_max = len(num)
    print(f'#{case} {count_max}')