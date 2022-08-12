for case in range(1, int(input())+1):
    cs, words_len = input().split()
    words_len = int(words_len)
    words = list(input().split())
    result = ''
    index = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for idx in index:
        result += (idx + ' ') * words.count(idx)
    print(f'#{case} {result}')