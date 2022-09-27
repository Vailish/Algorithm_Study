def caculate(node):  # 마지막 점부터 시작해서 올라감
    if node:
        left = caculate(tree[node][0])
        right = caculate(tree[node][1])
        # print(left, right, tree[node][2])
        if tree[node][2] == '+':
            return left + right
        elif tree[node][2] == '-':
            return left - right
        elif tree[node][2] == '*':
            return left * right
        elif tree[node][2] == '/':
            return int(left / right)
        else:
            return tree[node][2]


for case in range(1, 11):
    N = int(input())  # N = 정점의 수
    result = []
    tree = [[0]*3 for _ in range(N+1)]  # [[child1, child2, value],]
    # 트리 채우기
    for i in range(N):
        a, *b = input().split()
        a = int(a)
        if len(b) == 3:
            tree[a][2] = b[0]
            tree[a][1] = int(b[2])
            tree[a][0] = int(b[1])
        else:
            tree[a][2] = int(*b)

    print(f'#{case}', caculate(1))
