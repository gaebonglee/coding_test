N = int(input())
numbers = [int(input()) for _ in range(N)]

shorted_numbers = sorted(numbers)

for num in shorted_numbers:
    print(num)