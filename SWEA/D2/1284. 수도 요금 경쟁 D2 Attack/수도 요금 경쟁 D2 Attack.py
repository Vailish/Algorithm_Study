for case in range(1, 1+int(input())):
    p, q, r, s, w = map(int,input().split())

    a = p * w
    if w <= r:
        b = q
    else:
        b = q + s * (w - r)

    if a >= b:
        print(f'#{case} {b}')
    else:
        print(f'#{case} {a}')
