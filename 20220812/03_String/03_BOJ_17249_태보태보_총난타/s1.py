import sys
sys.stdin = open("input.txt")

punch = input()
num = 0
for k in punch:
    if k == '@':
        num += 1
    if k == '0':
        print(num, end=' ')
        num = 0
print(num)