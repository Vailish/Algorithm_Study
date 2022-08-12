for case in range(1, int(input())+1):
    N = int(input())
    nums = input().split('0')
    count_max = 0
    for num in nums:
        if count_max < len(num):
            count_max = len(num)
    print(f'#{case} {count_max}')