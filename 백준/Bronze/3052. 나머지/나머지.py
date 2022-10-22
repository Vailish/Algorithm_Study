rest = set()
for _ in range(10):
    number = int(input())
    rest.add(number % 42)
print(len(rest))
