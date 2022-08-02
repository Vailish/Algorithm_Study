# https://www.acmicpc.net/problem/10807
N = int(input())
lst = list(map(int, input().split()))
v = int(input())
result = lst.count(v)
print(result)