def d(n):
    return n + sum(map(int,str(n)))

self_numbers = [True] * 10001

for i in range(1, 10001):
    dn = d(i)
    if dn <= 10000:
        self_numbers[dn]= False

for i in range(1, 10001):
    if self_numbers[i]:
        print(i)