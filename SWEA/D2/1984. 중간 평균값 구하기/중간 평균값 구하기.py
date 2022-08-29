for case in range(1, 1 + int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop()
    arr.pop(0)
    print(f'#{case} {round(sum(arr)/len(arr))}')
