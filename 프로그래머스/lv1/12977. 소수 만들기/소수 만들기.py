def solution(nums):
    lst = []
    N = len(nums)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if i==j or j==k or k==i:
                    continue
                lst.append(nums[i] + nums[j] + nums[k])
    result = 0
    for number in lst:
        tmp = 0
        for n in range(1, number + 1):
            if number % n == 0:
                tmp += 1
        if tmp == 2:
            result += 1
    return result