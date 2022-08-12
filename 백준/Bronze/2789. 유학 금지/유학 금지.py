words = input()
result = ''
for word in words:
    if word not in ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']:
        result += word
print(result)