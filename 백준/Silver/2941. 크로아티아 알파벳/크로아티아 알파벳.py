word = input().strip()

croatia_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alpha in croatia_alphabets:
    word = word.replace(alpha, '*')

print(len(word))