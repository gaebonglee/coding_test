def second_largest(a,b,c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

a, b, c = map(int, input().split())

result = second_largest(a, b, c)
print(result)