def my_func(a, b):

    if b == 0:
        return ('input not zero')

    return a/b

a = int(input('input first number:'))
b = int(input('input second number:'))

print(my_func(a, b))