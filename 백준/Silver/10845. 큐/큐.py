import sys


class Queue:
    def __init__(self):
        self.value = []

    def push(self, x):
        self.value.append(x)

    def pop(self):
        if self.value:
            print(self.value.pop(0))
        else:
            print(-1)
    def size(self):
        print(len(self.value))

    def empty(self):
        if not self.value:
            print(1)
        else:
            print(0)

    def front(self):
        if self.value:
            print(self.value[0])
        else:
            print(-1)

    def back(self):
        if self.value:
            print(self.value[-1])
        else:
            print(-1)


que = Queue()
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == "push":
        que.push(int(command[1]))
    elif command[0] == "pop":
        que.pop()
    elif command[0] == "size":
        que.size()
    elif command[0] == "empty":
        que.empty()
    elif command[0] == "front":
        que.front()
    elif command[0] == "back":
        que.back()
