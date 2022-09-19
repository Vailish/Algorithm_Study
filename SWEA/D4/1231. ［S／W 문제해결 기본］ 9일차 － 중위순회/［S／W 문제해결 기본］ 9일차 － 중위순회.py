def inorder(n):
    global answer
    if n:
        inorder(left[n])
        answer += tree[n]
        inorder(right[n])

T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)  # 부모를 인덱스로 왼쪽 자식 저장
    right = [0] * (N+1) # 부모를 인덱스로 오른쪽 자식 저장
    tree = [0] * (N+1)  # 노드 데이터 저장
    for _ in range(N):
        arr = input().split()   # arr[0] 부모번호,...
        p = int(arr[0])         # 부모 번호
        tree[p] = arr[1]        # 데이터
        if len(arr)==4:
            left[p] = int(arr[2])   # 왼쪽 자식
            right[p] = int(arr[3])  # 오른쪽 자식
        elif len(arr)==3:
            left[p] = int(arr[2])  # 왼쪽 자식

        # if len(arr)>=3:
        #     left[p] = int(arr[2])  # 왼쪽 자식
        # if len(arr)==4:
        #     right[p] = int(arr[3])  # 오른쪽 자식
    answer = ''
    inorder(1)
    print(f'#{tc} {answer}')