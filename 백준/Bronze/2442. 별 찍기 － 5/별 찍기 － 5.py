starNum = int(input())

for i in range(starNum):

    print(' ' * (starNum - i - 1) + '*' * (2 * i + 1))
