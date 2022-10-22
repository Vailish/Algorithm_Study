h, m = map(int, input().split())
k = m - 45
if k >= 0:
    print(h, k)
else:
    if h == 0:
        print(23, 60 + k)
    else:
        print(h-1, 60 + k)
