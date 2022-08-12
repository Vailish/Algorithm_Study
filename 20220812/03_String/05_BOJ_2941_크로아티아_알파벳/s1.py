# 크로아티아 알파벳 실버5
# https://www.acmicpc.net/problem/2941

words = input()
# c= c- dz= d- lj nj s= z=

index = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for idx in index:
    words = words.replace(idx, '!')  # immutable이므로 대입해줘야함
print(len(words))