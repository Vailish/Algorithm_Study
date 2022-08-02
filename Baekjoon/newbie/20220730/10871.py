#https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())

lst = list(map(int, input().split()))
for num in lst:
    if X > num:
        print(num, end=" ")