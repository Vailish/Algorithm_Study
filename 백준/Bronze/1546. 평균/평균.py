n = int(input())
scores = list(map(int, input().split()))
print(sum(list(map(lambda x: x / max(scores) * 100, scores))) / n)