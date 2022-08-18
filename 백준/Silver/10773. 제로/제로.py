stack = []

for case in range(int(input())):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))