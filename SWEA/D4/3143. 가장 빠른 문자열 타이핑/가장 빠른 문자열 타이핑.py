for case in range(1, int(input()) + 1):
    A, B = input().split()
    # A안에 B를 !로 바꿔주기
    A = A.replace(B, '!')
    print(f'#{case} {len(A)}')