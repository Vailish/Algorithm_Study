T = int(input())

date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for case in range(T):
    year, month = map(int, input().split())
    if month == 3:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            condition = True
        else:
            condition = False

        print(year, 2, 29 if condition else 28)
    elif month == 1:
        print(year-1, 12, 31)
    else:
        print(year, month - 1, date[month - 1])
