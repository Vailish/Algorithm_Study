for _ in range(1, 1 + int(input())):
    case = int(input())
    arr = list(map(int, input().split()))
    mode = [0, 0]  # 최빈값 = [value, times]
    for num in sorted(list(set(arr))):
        if arr.count(num) >= mode[1]:
            mode[0] = num
            mode[1] = arr.count(num)
    print(f'#{case} {mode[0]}')
