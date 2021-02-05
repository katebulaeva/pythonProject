class Matrix:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        matrix = []

        for i in range(len(self.list)):
            matrix.append([])
            for j in range(len(self.list[i])):
                    matrix[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, matrix))

    def __str__(self):
        return '\n'.join((map(str, matrix)))


matrix1 = Matrix([[5, 10, 14], [6, 17, 23], [22, 33, 44]])
matrix2 = Matrix([[45, 8, 2], [6, 7, 89893], [11, 11, 11]])

print((matrix1 + matrix2))
