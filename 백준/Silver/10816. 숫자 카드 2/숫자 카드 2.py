import sys


def solution():
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    card_dict = {}
    for i in cards:
        if i in card_dict:
            card_dict[i] += 1
        else:
            card_dict[i] = 1
    M = int(sys.stdin.readline())
    checks = list(map(int, sys.stdin.readline().split()))
    return ' '.join(str(card_dict[x]) if x in card_dict else "0" for x in checks)


print(solution())