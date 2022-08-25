from collections import deque

N = int(input())
queue = deque(range(1, 1 + N))

while True:
    if len(queue) == 1:
        print(queue.popleft())
        break
    queue.popleft()
    queue.append(queue.popleft())
