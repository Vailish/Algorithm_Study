import sys
input = sys.stdin.readline


cnt_lst = [0] * 10001
for n in range(int(input())):
    cnt_lst[int(input())] += 1

for number in range(1, 10001):
    if cnt_lst[number] != 0:
        for _ in range(cnt_lst[number]):
            print(number)
