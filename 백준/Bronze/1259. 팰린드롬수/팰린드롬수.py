while True:
    numbers = list(input())
    if numbers == list('0'):
        break
    if numbers == numbers[::-1]:
        print('yes')
    else:
        print('no')
