chara = input()
cnt = []
cnt_lst = [0]*100
for c in chara:
    cnt_lst[int(ord(c.upper()))] += 1
max_numb = max(cnt_lst)
if cnt_lst.count(max(cnt_lst)) == 1:
    print(chr(cnt_lst.index(max_numb)))
else:
    print('?')

