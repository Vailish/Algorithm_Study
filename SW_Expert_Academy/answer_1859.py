T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr)-1,-1,-1): # 핵심! 뒤부터 보기
        if last > arr[i]:
            cnt += last-arr[i]
        else: # 같거나 작을 때 
            last = arr[i]
    print("#{} {}".format(t, cnt))