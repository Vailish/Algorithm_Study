def chk(n):
    cnt = 0
    for i in range(1, n+1):  # 1부터 n까지 나눠봄
        if n % i == 0:
            cnt += 1
    return True if cnt == 2 else False


answer = []
N = int(input())
nums = list(map(int, input().split()))
for k in range(N):
    num = nums[k]
    if chk(num):
        answer.append(num)

print(len(answer))
