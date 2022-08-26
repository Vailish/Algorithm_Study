def palindrome(words):
    return 1 if words == words[::-1] else 0


for case in range(1, 1 + int(input())):
    print(f'#{case} {palindrome(input())}')