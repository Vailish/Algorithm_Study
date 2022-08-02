# https://www.acmicpc.net/problem/5597
lst = list(range(1, 31))
for _ in range(28):
    lst.remove(int(input()))
print(min(lst))
lst.remove(min(lst))
print(min(lst))