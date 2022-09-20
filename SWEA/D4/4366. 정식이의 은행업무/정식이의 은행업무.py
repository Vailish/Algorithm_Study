dic_2 = {'0': '1',
         '1': '0'}
dic_3_1 = {'0': '1',
           '1': '2',
           '2': '0'}
dic_3_2 = {'0': '2',
           '1': '0',
           '2': '1'}

for case in range(1, 1 + int(input())):
    data_2 = input()
    data_3 = input()

    # 2진수 한 자리 변경
    for num in range(len(data_2)):
        value = data_2[:num] + dic_2.get(data_2[num]) + data_2[num + 1:]
        # 3진수로 변경
        value_10 = int(value, 2)  # 10진수로 변경
        rev_base = ''
        while value_10 > 0:
            value_10, mod = divmod(value_10, 3)
            rev_base += str(mod)
        value_3 = rev_base[::-1]

        # 기 3진수 값이랑 비교
        result = 0
        answer = False
        for num2 in range(len(data_3)):
            value_2 = data_3[:num2] + dic_3_1.get(data_3[num2]) + data_3[num2 + 1:]
            if value_2 == value_3:
                result = int(value_2, 3)
                answer = True
                break
        if answer == False:
            for num2 in range(len(data_3)):
                value_2 = data_3[:num2] + dic_3_2.get(data_3[num2]) + data_3[num2 + 1:]
                if value_2 == value_3:
                    result = int(value_2, 3)
                    break
        if result:
            print(f'#{case} {result}')
            break
