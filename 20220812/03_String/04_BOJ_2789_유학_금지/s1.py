# 1. 문자열 더하기를 이용
words = input()
result = ''
for word in words:
    if word not in 'CAMBRIDGE':
        result += word
print(result)
