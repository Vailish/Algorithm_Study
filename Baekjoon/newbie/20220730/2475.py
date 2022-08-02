#https://www.acmicpc.net/problem/2475

a, b, c, d, e = list(map(int, input().split()))
print((a**2 + b**2 + c**2 + d**2 + e**2)%10)