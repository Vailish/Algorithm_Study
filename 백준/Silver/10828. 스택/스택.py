import sys


class Stack:
    def __init__(self):
        self.value = []

    def push(self, x):
        self.value.append(x)

    def pop(self):
        if self.value:
            print(self.value.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.value))

    def empty(self):
        if not self.value:
            print(1)
        else:
            print(0)

    def top(self):
        if self.value:
            print(self.value[-1])
        else:
            print(-1)


stack = Stack()
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == "push":
       stack.push(command[1])
    elif command[0] == "pop":
        stack.pop()
    elif command[0] == "size":
        stack.size()
    elif command[0] == "empty":
        stack.empty()
    elif command[0] == "top":
        stack.top()
