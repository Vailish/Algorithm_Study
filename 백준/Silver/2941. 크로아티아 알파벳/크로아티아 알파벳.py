words = input()
index = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for idx in index:
    words = words.replace(idx, '!')  # immutable이므로 대입해줘야함
print(len(words))