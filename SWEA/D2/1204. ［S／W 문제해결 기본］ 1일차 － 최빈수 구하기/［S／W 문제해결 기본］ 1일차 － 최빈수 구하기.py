for _ in range(1, 1+int(input())):
    case = int(input())
    scores = list(map(int, input().split()))
    cnt = [0] * 101
    for score in scores:
        cnt[score] += 1
    tmp = 0
    answer = 0
    for num in range(len(cnt)):
        if tmp <= cnt[num]:
            answer = num
            tmp = cnt[num]
    print(f'#{case}', answer)
