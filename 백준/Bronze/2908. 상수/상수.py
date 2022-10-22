A, B = map(list, input().split())
for n in range(len(A)-1, -1, -1):
    if A[n] > B[n]:
        print(''.join(A[::-1]))
        break
    elif A[n] < B[n]:
        print(''.join(B[::-1]))
        break
