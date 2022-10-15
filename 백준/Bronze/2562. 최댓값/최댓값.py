numbers = []
for n in range(9):
    numbers.append(int(input()))
max_number = max(numbers)
print(max_number)
print(numbers.index(max_number) + 1)
