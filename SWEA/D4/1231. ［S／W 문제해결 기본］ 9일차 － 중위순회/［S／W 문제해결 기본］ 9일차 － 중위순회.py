def inorder(v):
    global answer
    if v <= N:
        inorder( v * 2)     # 왼쪽 서브트리의 루트로 이동
        answer += tree[v]
        inorder( v * 2 + 1) # 오른쪽 서브트리의 루트로 이동

T = 10
for tc in range(1, T+1):
    N = int(input())        # 정점 개수
    tree = [0] * (N+1)      # 완전이진트리
    for _ in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
    answer = ''
    inorder(1)      # 완전이진트리의 루트부터 순회
    print(f'#{tc} {answer}')