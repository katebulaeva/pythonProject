def my_func(a, b, c):
    if a < b and (b < c or b > c):
        return b + c
    elif a > b and b < c:
        return a + c
    elif a > b and b > c:
        return b + a

a = int(input('input first nubmer '))
b = int(input('input second nubmer '))
c = int(input('input third nubmer '))
print(my_func(a, b, c))

