front = 999
back = 999
while True:
    data = float(input())
    if data == 999:
        break
    if front != 999:
        back = front
    front = data

    if back != 999:
        print(format(front - back, '.2f'))
