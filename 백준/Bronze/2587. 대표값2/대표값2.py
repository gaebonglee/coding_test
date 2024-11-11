numbers = [int(input()) for _ in range(5)]
numbers.sort()
average = sum(numbers) // 5 
median = numbers[2]

print(average)
print(median)