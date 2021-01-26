def summary():
    try:
        with open('file5.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')

summary()