start_time = input()
end_time = input()

# 초 구하기
tmp = int(end_time[6:8]) - int(start_time[6:8])
minus_min = 0
if tmp < 0:
    second = '00' + str(60 + tmp) + '0'
    minus_min = -1
else:
    second = '00' + str(tmp) + '0'

# 분 구하기
tmp = int(end_time[3:5]) - int(start_time[3:5]) + minus_min
minus_hour = 0
if tmp < 0:
    minute = '00' + str(60 + tmp) + '0'
    minus_hour = -1
else:
    minute = '00' + str(tmp) + '0'

# 시간 구하기
tmp = int(end_time[0:2]) - int(start_time[0:2]) + minus_hour
if tmp < 0:
    hour = '00' + str(24 + tmp) + '0'
else:
    hour = '00' + str(tmp) + '0'

print(f'{hour[-3:-1]}:{minute[-3:-1]}:{second[-3:-1]}')
