students = list(range(1, 31))

submit= []

for _ in range(28):
    submit.append(int(input()))

for num in submit:
    students.remove(num)

for student in students:
    print(student)