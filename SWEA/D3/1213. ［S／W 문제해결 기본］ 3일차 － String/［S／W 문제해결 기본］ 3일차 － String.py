for _ in range(1, 11):
    case = int(input())
    index = input()
    words = input()
    words = words.replace(index, '!')
    print(f'#{case} {words.count("!")}')