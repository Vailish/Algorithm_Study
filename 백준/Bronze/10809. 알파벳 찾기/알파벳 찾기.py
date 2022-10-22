# ASCII 97 ~ 122 = a ~ z / ord(), chr()
chara = input()
for n in range(97, 122 + 1):
    if chr(n) in chara:
        print(chara.index(chr(n)), end=' ')
    else:
        print(-1, end=' ')
print()
