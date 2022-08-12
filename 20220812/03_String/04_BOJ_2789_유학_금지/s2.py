# 2. list와 remove 활용
words = list(input())
result = words[:]
for word in words:
    if word in ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']:
        result.remove(word)
print(''.join(result))
