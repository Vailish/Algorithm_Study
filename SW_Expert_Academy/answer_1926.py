N = int(input())

for i in range(1, N+1) :
    clap = 0
    j = str(i)
    if '3' in j or '6' in j or '9' in j :
        clap += j.count('3')
        clap += j.count('6')
        clap += j.count('9')
        for _ in range(clap) :
            print('-', end='')
        print(' ', end='')
    else :
        print(i, end=' ')