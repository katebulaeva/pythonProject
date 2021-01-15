num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new = [num[i] for i in range(len(num)) if num[i] > num[i-1] if i != 0]

print(new)