# 1976 여행 가자 골드4
# https://www.acmicpc.net/problem/1976

import sys
input = sys.stdin.readline


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(a, b):
    a = find_set(a)
    b = find_set(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())  # 도시 수
M = int(input())  # 여행계획에 속한 도시 수

# 길이 있다 == 같은 집합이다 -> Union이다
parent = list(range(N+1))  # [0, 1, 2, 3]
edges = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if edges[i-1][j-1] == 1:
            union(i, j)

switch = False
for num in range(M-1):
    if find_set(plan[num]) != find_set(plan[num+1]):
        switch = True
        break

print('YES' if switch==False else 'NO')