rus = {'One': 'Odin', 'Two': 'Dva', 'Three': 'Tri', 'Four': 'Chetire'}
new_file = []
with open('file4.txt', 'r') as f:
    for i in f:

        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])

with open('file4new.txt', 'w') as f2:
    f2.writelines(new_file)