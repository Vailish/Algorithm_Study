def solution():
    min, max = map(int, input().split())
    for num in range(min, max + 1):
        if num == 1:
            continue
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                break
        else:
            print(num)

solution()