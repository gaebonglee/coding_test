starNum = int(input())

for i in range(starNum):
    print(' ' * (starNum - i - 1) + '*' * (2 * i + 1))


for i in range(starNum - 1):
    print(' ' * (i + 1) + '*' * (2 * (starNum - i - 2) + 1))