def my_sum():
    sum = 0
    exit = False
    while exit == False:
        numbers = input('Input numbers or X for quit - ').split()

        res = 0
        for i in range(len(numbers)):
            if numbers[i] == 'x' or numbers[i] == 'X':
                exit = True
                break
            else:
                res = res + int(numbers[i])
        sum = sum + res
        print(f'Current sum is {sum}')
    print(f'Your final sum is {sum}')


my_sum()