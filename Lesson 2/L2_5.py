my_list = [7, 5, 3, 3, 2]
print(f"Rate - {my_list}")
digit = int(input("input number (9999 - exit) "))
while digit != 9999:
    for i in range(len(my_list)):
        if my_list[i] == digit:
            my_list.insert(i + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[i] > digit and my_list[i + 1] < digit:
            my_list.insert(i + 1, digit)
    print(f"List - {my_list}")
    digit = int(input("Input number "))