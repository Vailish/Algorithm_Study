number = 1
for _ in range(3):
    number *= int(input())

result = [0] * 10
for k in str(number):
    result[int(k)] += 1
for n in range(10):
    print(result[n])