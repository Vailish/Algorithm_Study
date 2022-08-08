T = int(input())

for case in range(1, T+1):
    test_case = list(map(int,input().split()))
    print(f'#{case} {round(sum(test_case)/len(test_case))}')