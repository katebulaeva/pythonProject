slovar = {}
with open('file6.txt', 'r') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()

        lecture = lecture.split('(')
        practice = practice.split('(')
        lab = lab.split('(')

        slovar[subject] = int(lecture[0]) + int(practice[0]) + int(lab[0])



    print(f'Общее количество часов по предметам - \n {slovar}')
