with open('file3.txt', 'r') as f:
    salary = []
    min = []
    my_list = f.read().split('\n')
    print(my_list)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           min.append(i[0])
        salary.append(i[1])


print(f'Оклад меньше 20.000 у {min}, средний оклад {sum(map(int, salary)) / len(salary)}')