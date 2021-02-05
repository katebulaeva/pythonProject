with open('file2.txt', 'r') as f:
    content = f.readlines()
    print(content, '\n')
    print(f'The number of rows in file are - {len(content)}\n')

with open('file2.txt', 'r') as f:
        for num, line in enumerate(f,1):

            words = len(line.split())
            print(f'The number of words in string {num} are {words}')

