def second_largest(a,b,c):
    if (a >= b and a <= c) or (a >= c and a <= b):
        return a
    elif (b >= a and b <= c) or (b >= c and b <= a):
        return b
    else:
        return c

a, b, c = map(int, input().split())


result = second_largest(a,b,c)
print(result)