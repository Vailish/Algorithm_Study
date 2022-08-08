T = int(input())
for case in range(1, T+1):
    A, B = map(int, input().split())
    if A > B:
        print(f'#{case} >')
    elif A < B:
        print(f'#{case} <')
    else:
        print(f'#{case} =')