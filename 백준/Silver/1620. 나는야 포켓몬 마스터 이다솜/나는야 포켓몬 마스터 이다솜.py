def solution():
    N, M = map(int, input().split())
    dic = dict()

    for num in range(1, N+1):
        val = input().rstrip()
        dic[val] = num
        dic[num] = val

    for i in range(M):
        key = input().rstrip()
        if key.isdigit():
            print(dic[int(key)])
        else: 
            print(dic[key])

solution()
