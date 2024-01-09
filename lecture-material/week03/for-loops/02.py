size = 6

for i in range(1, size * 2):
    if i <= size:
        print('X' * i)
    else:
        print('X' * (2 * size - i))

#Output