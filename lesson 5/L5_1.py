text = input('Input data (Empty - is End): ')
while text != (''):
    with open('file1.txt', 'a') as f:
        f.write(text + '\n')

        text = input('Input data: ')
