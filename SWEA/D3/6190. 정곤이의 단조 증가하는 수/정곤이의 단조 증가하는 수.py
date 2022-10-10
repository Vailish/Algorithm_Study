from itertools import permutations


def check(number):
    for i in range(0, len(number) - 1):
        if int(number[i]) > int(number[i+1]):
            return False
    return True


def solution():
    # 두 수를 뽑아 곱하기
    result = []
    for x, y in permutations(arr, 2):
        number = x * y
        # 단조 증가하는 수인지 검사
        if check(str(number)) == True:
            result.append(number)
    return max(result) if len(result) > 0 else -1


for case in range(1, 1 + int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{case}', solution())
