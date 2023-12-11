def solution():
    N, r, c = map(int,input().split())
    answer = 0
    while N > 0:
        v = 2**(N-1)
        vn = 4**(N-1)
        # 좌상인경우
        if r < v and c < v:
            answer += 0
        elif r < v and c >= v:
            answer += vn
            c -= v

        elif r >= v and c < v:
            answer += 2 * vn
            r -= v
        else:
            answer += 3 * vn
            r -= v
            c -= v
        N -= 1
    print(answer)


solution()
