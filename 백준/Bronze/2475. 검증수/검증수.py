numbers = list(map(int, input().split()))
total = sum([num ** 2 for num in numbers])
verification_number = total % 10
print(verification_number)